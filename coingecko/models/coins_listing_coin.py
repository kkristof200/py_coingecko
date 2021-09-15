# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional
from decimal import Decimal

# Pip


# Local
from .base_coin import BaseCoin

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: CoinsListingCoin ------------------------------------------------------- #

class CoinsListingCoin(BaseCoin):

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
        perc_change_30d: Optional[Decimal],
        volume_24h: Optional[Decimal],
        market_cap: Optional[Decimal],
        circulating_supply: Optional[Decimal],
        total_supply: Optional[Decimal],
        added_at: str
    ):
        super().__init__(
            name=name,
            symbol=symbol,
            img_url=img_url,
            price=price,
            price_btc=price_btc,
            perc_change_1h=perc_change_1h,
            perc_change_24h=perc_change_24h,
            perc_change_7d=perc_change_7d,
            volume_24h=volume_24h,
            market_cap=market_cap
        )

        self.perc_change_30d = perc_change_30d
        self.circulating_supply = circulating_supply
        self.total_supply = total_supply


# ---------------------------------------------------------------------------------------------------------------------------------------- #