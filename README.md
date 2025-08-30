# Fluent Telegrinder
[Fluent](https://projectfluent.org) i18n implementation for telegrinder

## Installation:
```shell
pip install fluent-telegrinder
```

## Usage:
```python
from telegrinder import API, Message, Telegrinder, Token
from telegrinder.node import as_node

from fluent_telegrinder import (
    DefaultLocaleSource,  # UserLanguageSource or custom source (any node, returns str)
    FluentConfig,
    FluentTranslator,  # or alias: Translator
    TextEquals,
)

config = FluentConfig(
    folder="locales/",
    source=as_node(DefaultLocaleSource), # source for locale
    default_locale="ru",
    replace_underscore=True, # i_love_telegrinder -> i-love-telegrinder
)
FluentTranslator.configure(config)

bot = Telegrinder(API(Token.from_env()))

@bot.on.message(TextEquals("hello", ignore_case=True)) # hello - i18n key (hello, привет)
async def on_hello(msg: Message, _: FluentTranslator):
    await msg.reply(_.hello_answer(user=msg.from_user.first_name))

bot.run_forever(skip_updates=True)
```

## License
Fluent Telegrinder licensed under [MIT license](./LICENSE)
