import requests
from dataclasses import dataclass


@dataclass
class IKEApi:
    """IKEApi provider class."""

    category: int = 20652
    size: int = 1_000_000
    c: str = "lf"
    v: int = 20220826
    sort: str = "RELEVANCE"
    store: int = 204
    zip: str = "30-363"

    @property
    def api_base_url(self) -> str:
        return "https://sik.search.blue.cdtapps.com/pl/pl/product-list-page"

    @property
    def query_params(self) -> dict:
        return self.__dict__

    def fetch(self) -> dict:
        try:
            response = requests.get(self.api_base_url, params=self.query_params)
        except requests.exceptions.RequestException as e:
            return {"error": e}
        return response.json()
