# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional
from decimal import Decimal
import time

# Pip
from kcu import ktime

# Local
from .base_coin import BaseCoin

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------- class: RecentlyAddedCoin ------------------------------------------------------- #

class RecentlyAddedCoin(BaseCoin):

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
        market_cap: Optional[Decimal],
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
        
        self.approximate_added_at_ts = self.__parse_added_at_text(added_at)


    # ------------------------------------------------------ Public properties ------------------------------------------------------- #

    @property
    def approximate_age_seconds(self) -> int:
        return int(time.time()) - self.approximate_added_at_ts


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    def __parse_added_at_text(self, s: str) -> int:
        base_val = int(''.join([c for c in s if c.isdigit()]))

        if 'hour' in s:
            return int(time.time()) - base_val * ktime.seconds_in_hour

        if 'day' in s:
            return int(time.time()) - base_val * ktime.seconds_in_day

        return int(time.time()) - base_val * ktime.seconds_in_day * 30


# ---------------------------------------------------------------------------------------------------------------------------------------- #