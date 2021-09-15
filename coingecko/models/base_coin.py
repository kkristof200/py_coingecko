# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional
from decimal import Decimal

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: BaseCoin ----------------------------------------------------------- #

class BaseCoin:

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        name: str,
        symbol: str,
        img_url: str,
        price: Decimal,
        price_btc: Decimal,
        perc_change_1h: Optional[Decimal],
        perc_change_24h: Optional[Decimal],
        perc_change_7d: Optional[Decimal],
        volume_24h: Optional[Decimal],
        market_cap: Optional[Decimal]
    ):
        self.name = name
        self.symbol = symbol
        self.img_url = img_url
        self.price = price
        self.price_btc = price_btc
        self.perc_change_1h = perc_change_1h
        self.perc_change_24h = perc_change_24h
        self.perc_change_7d = perc_change_7d
        self.volume_24h = volume_24h
        self.market_cap = market_cap
        self.curculating_supply = market_cap / price if market_cap else None


# ---------------------------------------------------------------------------------------------------------------------------------------- #