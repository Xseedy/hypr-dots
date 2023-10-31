config.load_autoconfig(False)

# bindings.commands = {"normal": {";w": "hint links spawn --detach mpv --force-window yes {hint-url}", "pt": "pin-tab"}}
config.bind('pt', 'tab-pin')
config.bind(';w','hint links spawn --detach mpv --force-window yes {hint-url}')
config.bind(';W','spawn --detach mpv --force-window yes {url}')
config.bind(';I','hint images spawn --output-messages wget -P "/home/seed/Downloads/" {hint-url}')
# password management
config.bind('ee','spawn --userscript qute-pass')
config.bind('eu','spawn --userscript qute-pass --username-only')
config.bind('ep','spawn --userscript qute-pass --password-only')
config.bind('eo','spawn --userscript qute-pass --otp-only')

c.colors.tabs.even.bg = 'grey'
c.colors.tabs.odd.bg = 'darkgrey'

c.content.pdfjs = True
c.content.autoplay = False

c.editor.command = ["st", "-e", "vim", "{file}", "-c", "normal {line}G{column0}l"]

c.tabs.background = True
c.tabs.title.format_pinned = '{index} {audio}'

c.url.open_base_url = False
c.url.start_pages = 'https://duckduckgo.com/'
c.url.default_page = 'about:blank'

c.url.searchengines = {"DEFAULT": "https://duckduckgo.com/?q={}",
        "ksl": "https://classifieds.ksl.com/search?keyword={}",
        "tw": "https://twitch.tv/{}",
        "dlive": "https://dlive.tv/{}",
        "ig": "https://infogalactic.com/w/index.php?search={}",
        "yt": "https://www.youtube.com/results?search_query={}"}

c.window.title_format = '{perc}{current_title}{title_sep}seed browser'
