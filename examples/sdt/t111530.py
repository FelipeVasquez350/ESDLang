# -*- coding: utf-8 -*-
def t111530_1():
    """State 0"""
    while True:
        """State 1"""
        if GetEventStatus(8302) == 1:
            """State 3,5"""
            # talk:60003100:"([Buddhist chanting] Namu Amida Butsu, Namu Amida Butsu...)"
            assert t111530_x7(actionbutton1=7009120, z1=71110601, text1=60003100)
        elif GetEventStatus(8301) == 1:
            """State 2,4"""
            # talk:60003000:"Hmm..."
            assert t111530_x7(actionbutton1=7009114, z1=71110600, text1=60003000)

def t111530_x0(actionbutton1=_, flag1=6001, flag2=6001, flag3=6001, flag4=6001, flag5=6001, actionbutton2=0,
               flag6=6000, val1=-1, val2=-1, val3=-1, val4=-1, val5=-1):
    """State 0"""
    while Loop('mainloop'):
        """State 3"""
        call = t111530_x10(actionbutton1=actionbutton1, flag1=flag1, flag2=flag2, flag3=flag3, flag4=flag4,
                           flag5=flag5, actionbutton2=actionbutton2, flag6=flag6)
        if call.Done():
            break
        elif (not f116(-1) == val1 and not f116(-1) == val2 and not f116(-1) == val3 and not DoesSelfHaveSpEffect(4510)
              and not val1 == -1 and not f116(-1) == val4 and not f116(-1) == val5):
            pass
        while True:
            """State 1"""
            assert (f116(-1) == val1 or f116(-1) == val2 or f116(-1) == val3 or (DoesSelfHaveSpEffect(4510)
                    == 1 and f116(-1) == val4 and f116(-1) == val5))
            """State 2"""
            if GetCurrentStateElapsedTime() > 0.5:
                Continue('mainloop')
            elif (not f116(-1) == val1 and not f116(-1) == val2 and not f116(-1) == val3 and not DoesSelfHaveSpEffect(4510)
                  and not f116(-1) == val4 and not f116(-1) == val5):
                pass
    """State 4"""
    SetTalkTime(0.1)
    return 0

def t111530_x1():
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

def t111530_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t111530_x3(text1=_, z1=_, flag7=0, mode1=1):
    """State 0,7"""
    assert t111530_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 5"""
    if not flag7:
        """State 1"""
        TalkToPlayer(text1, -1, -1, flag7, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 6"""
        TalkToPlayer(text1, -1, -1, flag7, 1)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode1:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventState(z1, 1)
    """State 8"""
    return 0

def t111530_x4():
    """State 0,2"""
    assert t111530_x1()
    """State 1"""
    ClearTalkProgressData()
    """State 3"""
    return 0

def t111530_x5(actionbutton1=_, z1=_, text1=_):
    """State 0"""
    while True:
        """State 1"""
        call = t111530_x6(actionbutton1=actionbutton1, z1=z1, text1=text1)
        assert not f114(2)
        """State 2"""
        assert t111530_x8() and f114(2) == 1
    """Unused"""
    """State 3"""
    return 0

def t111530_x6(actionbutton1=_, z1=_, text1=_):
    """State 0"""
    while True:
        """State 1,3"""
        assert (t111530_x0(actionbutton1=actionbutton1, flag1=6001, flag2=6001, flag3=6001, flag4=6001,
                flag5=6001, actionbutton2=0, flag6=6000, val1=-1, val2=-1, val3=-1, val4=-1, val5=-1))
        """State 2"""
        ClearPlayerDamageInfo()
        """State 4"""
        call = t111530_x9(text1=text1, z1=z1)
        def WhilePaused():
            c1_117(10, 10000)
        if call.Done():
            pass
        elif (HasPlayerBeenAttacked() == 1 or (GetTalkInterruptReason() == 5 and IsTalkInProgress() ==
              1) or IsPlayerDead() == 1):
            """State 5"""
            assert t111530_x4()
    """Unused"""
    """State 6"""
    return 0

def t111530_x7(actionbutton1=_, z1=_, text1=_):
    """State 0"""
    while True:
        """State 3"""
        assert t111530_x8() and (f113() < 0.5 and f116(-1) == 1000000)
        """State 1"""
        if GetCurrentStateElapsedTime() > 1:
            """State 2"""
            call = t111530_x5(actionbutton1=actionbutton1, z1=z1, text1=text1)
            def WhilePaused():
                c1_116()
            assert f113() > 1 or not f116(-1) == 1000000
        elif f113() > 1 or not f116(-1) == 1000000:
            pass
    """Unused"""
    """State 4"""
    return 0

def t111530_x8():
    """State 0,1"""
    assert t111530_x1()
    """State 2"""
    return 0

def t111530_x9(text1=_, z1=_):
    """State 0,1"""
    if f116(10000) == 10:
        """State 3"""
        call = t111530_x3(text1=text1, z1=z1, flag7=0, mode1=1)
        if call.Done():
            pass
        elif not f116(10000) == 10:
            pass
    elif not f116(10000) == 10 and GetCurrentStateElapsedTime() > 0.5:
        """State 2"""
        pass
    """State 4"""
    return 0

def t111530_x10(actionbutton1=_, flag1=6001, flag2=6001, flag3=6001, flag4=6001, flag5=6001, actionbutton2=0,
                flag6=6000):
    """State 0"""
    while Loop('mainloop'):
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventStatus(flag1) == 1 or GetEventStatus(flag2) == 1 or GetEventStatus(flag3) ==
                1 or GetEventStatus(flag4) == 1 or GetEventStatus(flag5) == 1)
        while True:
            """State 4"""
            assert not GetEventStatus(flag6)
            """State 2"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                Continue('mainloop')
            elif (not GetEventStatus(flag1) and not GetEventStatus(flag2) and not GetEventStatus(flag3)
                  and not GetEventStatus(flag4) and not GetEventStatus(flag5)):
                Continue('mainloop')
            elif GetEventStatus(flag6) == 1:
                pass
            elif CheckActionButtonArea(actionbutton1 + actionbutton2) and not f116(10000) == 90:
                Break('mainloop')
    """State 5"""
    SetTalkTime(0.1)
    return 0

