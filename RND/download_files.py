from gazpacho import get, Soup
from urlpath import URL
from pathlib import Path

KERNEL_VERSION = '5.10.3'
LINUX_SERVER_URL = 'https://elixir.bootlin.com/linux'
VKERNEL_VERSION = f'v{KERNEL_VERSION}'
PERF_PYTHON_PATH = 'source/tools/perf/scripts/python'
EVENT_ANALYZING_SAMPLE = 'event_analyzing_sample.py'
PERF_PYTHON_URL = URL(LINUX_SERVER_URL).joinpath(VKERNEL_VERSION, PERF_PYTHON_PATH).as_posix()
#https://elixir.bootlin.com/linux/v5.10.3/source/tools/perf/scripts/python/event_analyzing_sample.py


def list_files():
    soup = Soup(get(PERF_PYTHON_URL))
    all_links = [link.attrs["href"] for link in soup.find('a')]
    py_links = [link for link in all_links if link.endswith(".py")]
    return py_links


for x in list_files():
    print(x)

for y in list_files():
    print(URL(LINUX_SERVER_URL).joinpath(y))


