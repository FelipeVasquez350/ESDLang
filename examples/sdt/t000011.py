# -*- coding: utf-8 -*-
def t000011_1():
    """State 0,1"""
    t000011_x0()
    Quit()

def t000011_x0():
    """State 0"""
    while True:
        """State 2"""
        assert DoesSelfHaveSpEffect(4500) == 1 and f116(-1) == 1000000
        """State 3"""
        if GetCurrentStateElapsedTime() > 1:
            """State 1"""
            def WhilePaused():
                c1_116()
            assert not DoesSelfHaveSpEffect(4500) or not f116(-1) == 1000000
        elif not DoesSelfHaveSpEffect(4500) or not f116(-1) == 1000000:
            pass
    """Unused"""
    """State 4"""
    return 0

