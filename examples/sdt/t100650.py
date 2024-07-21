# -*- coding: utf-8 -*-
def t100650_1():
    """State 0,1"""
    if GetEventStatus(6502) == 1:
        pass
    else:
        """State 3"""
        # talk:65001300:"Woahh! Look at it burn!"
        call = t100650_x6(val1=10, val2=15, flag1=71008500, text1=65001300)
        assert GetEventStatus(6502) == 1
        """State 4"""
        assert t100650_x0()
    """State 2"""
    Quit()

def t100650_x0():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t100650_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t100650_x2(text1=65001300, flag1=71008500, flag2=1, mode1=1):
    """State 0,7"""
    assert t100650_x1() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(flag1, 1)
    """State 6"""
    if not flag2:
        """State 1"""
        # talk:65001300:"Woahh! Look at it burn!"
        TalkToPlayer(text1, -1, -1, flag2, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        # talk:65001300:"Woahh! Look at it burn!"
        TalkToPlayer(text1, -1, -1, flag2, 1)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode1:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 8"""
    return 0

def t100650_x3(flag1=71008500, text1=65001300, val1=10, val2=15):
    """State 0"""
    while True:
        """State 3"""
        assert t100650_x7() and (f116(-1) == 1000000 and f113() < 0.5)
        """State 1"""
        if GetCurrentStateElapsedTime() > 1:
            """State 2"""
            call = t100650_x4(flag1=flag1, text1=text1, val1=val1, val2=val2)
            def WhilePaused():
                c1_116()
            if call.Done():
                break
            elif not f116(-1) == 1000000 or f113() > 1:
                pass
        elif not f116(-1) == 1000000 or f113() > 1:
            pass
    """State 4"""
    return 0

def t100650_x4(flag1=71008500, text1=65001300, val1=10, val2=15):
    """State 0"""
    while True:
        """State 1"""
        call = t100650_x5(flag1=flag1, text1=text1, val1=val1, val2=val2)
        if call.Done():
            break
        elif not f114(2):
            """State 2"""
            assert t100650_x7() and f114(2) == 1
    """State 3"""
    return 0

def t100650_x5(flag1=71008500, text1=65001300, val1=10, val2=15):
    """State 0,1"""
    assert GetDistanceToPlayer() < val1
    """State 3"""
    call = t100650_x2(text1=text1, flag1=flag1, flag2=1, mode1=1)
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val2:
        """State 2"""
        assert t100650_x7()
    """State 4"""
    return 0

def t100650_x6(val1=10, val2=15, flag1=71008500, text1=65001300):
    """State 0"""
    while True:
        """State 1"""
        if GetEventStatus(flag1) == 1:
            """State 2"""
            assert not GetEventStatus(flag1)
        elif not GetEventStatus(flag1):
            """State 3"""
            assert t100650_x3(flag1=flag1, text1=text1, val1=val1, val2=val2)
    """Unused"""
    """State 4"""
    return 0

def t100650_x7():
    """State 0,1"""
    assert t100650_x0()
    """State 2"""
    return 0

