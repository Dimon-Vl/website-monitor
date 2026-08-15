import requests
from requests.exceptions import RequestException
from model import Website_Res

def get_status_from_status_code(status_code: int) -> str:
    status_code = int(status_code)
    if 200 <= status_code < 400:
        return "UP"
    if 400 <= status_code < 500:
        return "ERROR"
    return "DOWN"

def sync_check_website(url: str, time_out: float = 2) -> Website_Res:
    try:
        r = requests.get(url, timeout=time_out)
    except RequestException as er:
        return Website_Res(
            url=url,
            status="DOWN",
            status_code=None,
            response_time=None,
            error=f"{type(er).__name__}: {er}",
        )

    return Website_Res(
        url=r.url,
        status=get_status_from_status_code(r.status_code),
        status_code=r.status_code,
        response_time=round(r.elapsed.total_seconds()* 1000),
        error=None,
    )
