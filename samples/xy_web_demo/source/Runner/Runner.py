# -*- coding: utf-8 -*-
__doc__ = "Runner.py"
__version__ = "0.0.1"

from xy_work.Work import Work


class Runner(Work):
    @property
    def __version__(self) -> str:
        return __version__

    def get_name(self) -> str:
        return "xy_web_demo"

    def __init__(self, *args, **kwargs) -> None:
        description: str = f""">>>>>>>>>>>> {self.get_name()} - v{self.__version__} <<<<<<<<<<<<<"""
        print(description)
        print()
        print("Hello World!!!")