from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader
from telegrinder.node import IsNode


@dataclass
class FluentConfig:
    folder: Path | str
    source: IsNode
    default_locale: str = "en"
    replace_underscore: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.folder, Path):
            self.folder = Path(self.folder)

    @cached_property
    def loaders(self) -> dict[str, FluentLocalization]:
        result: dict[str, FluentLocalization] = {}

        for locale_dir in self.folder.iterdir(): # type: ignore
            if not locale_dir.is_dir():
                continue

            ftl_files = [p.name for p in locale_dir.glob("*.ftl")]
            if not ftl_files:
                continue

            loader = FluentResourceLoader(str(self.folder / "{locale}")) # type: ignore
            result[locale_dir.name] = FluentLocalization(
                locales=[locale_dir.name],
                resource_ids=ftl_files,
                resource_loader=loader,
            )

        return result

    def get_translator(self, locale: str) -> FluentLocalization:
        return self.loaders.get(locale, self.loaders[self.default_locale])
