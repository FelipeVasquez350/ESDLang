# -*- coding: utf-8 -*-
def t250390_1():
    """State 0,1"""
    t250390_x6(flag1=1779, flag2=1775, flag3=1776, val1=5, val2=10, val3=12, val4=10, val5=12, flag4=6000,
               actionbutton1=7003900, flag5=1775, flag6=6001, flag7=72500160, flag8=6000, mode1=1, val6=1000000,
               val7=1000000, val8=1000000, mode2=1, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0,
               flag9=6000, mode6=0)
    Quit()

def t250390_1000():
    """State 0,4"""
    assert f116(-1) == 1000000
    """State 2,3"""
    if not GetEventStatus(72500150):
        """State 5"""
        # talk:39000000:"Young man, do you happen to be going to the palace?"
        assert t250390_x4(text2=39000000, z2=72500150, flag15=0, mode12=1)
    elif GetEventStatus(72500150) == 1 and not GetEventStatus(72500151):
        """State 6"""
        # talk:39000100:"Why are you helping me..?"
        assert t250390_x4(text2=39000100, z2=72500151, flag15=0, mode12=1)
    else:
        """State 7"""
        # talk:39000200:"Nowadays it's under water, but there is a large cave that will take you to the palace.\nOnly, I hear the Great Carp now sleeps there..."
        assert t250390_x5(text1=39000200, flag14=0, mode11=1)
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t250390_1100():
    """State 0,2"""
    SetEventState(72500160, 0)
    """State 3"""
    SetEventState(72500170, 1)
    """State 4"""
    call = t250390_x28()
    if call.Done():
        pass
    elif GetDistanceToPlayer() < 3:
        """State 5"""
        assert t250390_x1()
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t250390_2000():
    """State 0,3"""
    assert (t250390_x0(actionbutton1=7003900, flag6=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
            actionbutton2=0, flag5=6000, val6=1000000, val7=1000000, val8=1000000, val9=1000000, val10=1000000))
    """State 2"""
    SetEventState(72500170, 1)
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t250390_x0(actionbutton1=7003900, flag6=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
               actionbutton2=0, flag5=_, val6=1000000, val7=1000000, val8=1000000, val9=1000000, val10=1000000):
    """State 0"""
    while Loop('mainloop'):
        """State 3"""
        call = t250390_x27(actionbutton1=actionbutton1, flag6=flag6, flag10=flag10, flag11=flag11, flag12=flag12,
                           flag13=flag13, actionbutton2=actionbutton2, flag5=flag5)
        if call.Done():
            break
        elif (not f116(-1) == val6 and not f116(-1) == val7 and not f116(-1) == val8 and not DoesSelfHaveSpEffect(4510)
              and not val6 == -1 and not f116(-1) == val9 and not f116(-1) == val10):
            pass
        while True:
            """State 1"""
            assert (f116(-1) == val6 or f116(-1) == val7 or f116(-1) == val8 or (DoesSelfHaveSpEffect(4510)
                    == 1 and f116(-1) == val9 and f116(-1) == val10))
            """State 2"""
            if GetCurrentStateElapsedTime() > 0.5:
                Continue('mainloop')
            elif (not f116(-1) == val6 and not f116(-1) == val7 and not f116(-1) == val8 and not DoesSelfHaveSpEffect(4510)
                  and not f116(-1) == val9 and not f116(-1) == val10):
                pass
    """State 4"""
    SetTalkTime(0.1)
    return 0

def t250390_x1():
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

def t250390_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t250390_x3(text3=_, z3=_, flag16=1, mode13=1):
    """State 0,7"""
    assert t250390_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z3, 1)
    """State 6"""
    if not flag16:
        """State 1"""
        TalkToPlayer(text3, -1, -1, flag16, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        TalkToPlayer(text3, -1, -1, flag16, 1)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode13:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 8"""
    return 0

def t250390_x4(text2=_, z2=_, flag15=0, mode12=1):
    """State 0,7"""
    assert t250390_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 5"""
    if not flag15:
        """State 1"""
        TalkToPlayer(text2, -1, -1, flag15, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 6"""
        TalkToPlayer(text2, -1, -1, flag15, 1)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode12:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventState(z2, 1)
    """State 8"""
    return 0

def t250390_x5(text1=39000200, flag14=0, mode11=1):
    """State 0,6"""
    assert t250390_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not flag14:
        """State 1"""
        # talk:39000200:"Nowadays it's under water, but there is a large cave that will take you to the palace.\nOnly, I hear the Great Carp now sleeps there..."
        TalkToPlayer(text1, -1, -1, flag14, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        # talk:39000200:"Nowadays it's under water, but there is a large cave that will take you to the palace.\nOnly, I hear the Great Carp now sleeps there..."
        TalkToPlayer(text1, -1, -1, flag14, 1)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode11:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 7"""
    return 0

def t250390_x6(flag1=1779, flag2=1775, flag3=1776, val1=5, val2=10, val3=12, val4=10, val5=12, flag4=6000,
               actionbutton1=7003900, flag5=1775, flag6=6001, flag7=72500160, flag8=6000, mode1=1, val6=1000000,
               val7=1000000, val8=1000000, mode2=1, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0,
               flag9=6000, mode6=0):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t250390_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, flag4=flag4, actionbutton1=actionbutton1,
                          flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, mode1=mode1, val6=val6,
                          val7=val7, val8=val8, mode2=mode2, mode3=mode3, mode4=mode4, val9=val9, val10=val10,
                          mode5=mode5, mode6=mode6)
        def WhilePaused():
            c5_116(GetDistanceToPlayer() < 4)
        if (CheckSelfDeath() == 1 or GetEventStatus(flag1) == 1) and not GetEventStatus(flag9):
            pass
        elif GetEventStatus(flag2) == 1 or GetEventStatus(flag3) == 1:
            """State 3"""
            call = t250390_x22(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventStatus(flag1) == 1 or DoesSelfHaveSpEffect(30100) == 1:
                pass
            elif not GetEventStatus(flag2) and not GetEventStatus(flag3):
                continue
        """State 2"""
        call = t250390_x8(flag1=flag1, val2=val2, val3=val3)
        assert not CheckSelfDeath() and not GetEventStatus(flag1) and not DoesSelfHaveSpEffect(30100)
    """Unused"""
    """State 4"""
    return 0

def t250390_x7(val1=5, val2=10, val3=12, val4=10, val5=12, flag4=6000, actionbutton1=7003900, flag5=1775,
               flag6=6001, flag7=72500160, flag8=6000, mode1=1, val6=1000000, val7=1000000, val8=1000000,
               mode2=1, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0, mode6=0):
    """State 0"""
    while True:
        """State 4"""
        call = t250390_x24(actionbutton1=actionbutton1, flag5=flag5, flag6=flag6, val6=val6, val7=val7,
                           val8=val8, val9=val9, val10=val10)
        if call.Done():
            """State 1"""
            Label('L0')
            call = t250390_x9(val1=val1, mode1=mode1, mode2=mode2, mode3=mode3, mode4=mode4, mode5=mode5)
            def WhilePaused():
                GiveSpEffectToPlayer(30700)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
                pass
        elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
            pass
        elif GetEventStatus(flag8) == 1:
            Goto('L0')
        elif not GetEventStatus(flag4) and GetEventStatus(flag7) == 1 and GetDistanceToPlayer() < val4:
            """State 3"""
            call = t250390_x10(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
                pass
        """State 2"""
        def ExitPause():
            RemoveMyAggro()
        assert t250390_x11(val2=val2, val3=val3)
    """Unused"""
    """State 5"""
    return 0

def t250390_x8(flag1=1779, val2=10, val3=12):
    """State 0,1"""
    if GetEventStatus(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t250390_x19()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3:
                """State 7"""
                assert t250390_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t250390_x9(val1=5, mode1=1, mode2=1, mode3=1, mode4=0, mode5=0):
    """State 0,2"""
    ClearPlayerDamageInfo()
    TurnCharacterToFaceEntity(-1, 10000, -1)
    call = t250390_x17(mode2=mode2, mode4=mode4)
    def WhilePaused():
        c1_117(mode1, 10000)
        c1_117(1000000, -1)
        SetTalkTime(0.01)
        SetMenuDisableTimeIf(mode3 == 1, 0.1)
        c5_120(val1 == 1 and not mode1 and mode5 == 1, 1, 0, 9, 9, 9, 9, 9, 9, 9)
    if call.Done():
        pass
    elif (HasPlayerBeenAttacked() == 1 or (GetTalkInterruptReason() == 5 and IsTalkInProgress() == 1)
          or IsPlayerDead() == 1 or f116(10000) == 90):
        """State 1"""
        assert t250390_x14()
    elif GetDistanceToPlayer() > val1:
        """State 3"""
        assert t250390_x13()
    """State 4"""
    return 0

def t250390_x10(val5=12):
    """State 0,1"""
    call = t250390_x23()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5:
        """State 2"""
        assert t250390_x1()
    """State 3"""
    return 0

def t250390_x11(val2=10, val3=12):
    """State 0,4"""
    assert t250390_x1() and GetCurrentStateElapsedFrames() > 2
    """State 1"""
    if GetDistanceToPlayer() < 10:
        """State 2,6"""
        call = t250390_x16()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 5"""
            assert t250390_x1()
    else:
        """State 3"""
        pass
    """State 7"""
    return 0

def t250390_x12(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 2"""
    call = t250390_x21()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 3"""
        assert t250390_x1()
    """State 4"""
    return 0

def t250390_x13():
    """State 0,1"""
    assert t250390_x1()
    """State 2"""
    return 0

def t250390_x14():
    """State 0,2"""
    assert t250390_x1()
    """State 1"""
    ClearTalkProgressData()
    """State 3"""
    return 0

def t250390_x15(val2=10, val3=12):
    """State 0,2"""
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t250390_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3:
            """State 4"""
            assert t250390_x1()
    """Unused"""
    """State 5"""
    return 0

def t250390_x16():
    """State 0,1"""
    assert t250390_x18(z1=1101, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t250390_x17(mode2=1, mode4=0):
    """State 0,2"""
    if f116(10000) == 1:
        """State 1"""
        assert GetCurrentStateElapsedFrames() > 5
        """State 3"""
        assert not DoesPlayerHaveSpEffect(4511)
        """State 4"""
        def WhilePaused():
            c5_120(mode2 == 1 and not mode4, 1, 0, 9, 9, 9, 9, 9, 9, 9)
            c5_120(mode2 == 1 and mode4 == 1, 2, 9, 0, 9, 9, 9, 9, 9, 9)
        assert t250390_x18(z1=1000, mode7=0, mode8=0, mode9=0, mode10=0)
    elif GetCurrentStateElapsedTime() > 5:
        pass
    """State 5"""
    return 0

def t250390_x18(z1=_, mode7=0, mode8=0, mode9=0, mode10=0):
    """State 0,4"""
    if f118(z1) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 1"""
        def WhilePaused():
            c1_118(z1)
        assert f117() == mode7 or f117() == mode8 or f117() == mode9 or f117() == mode10
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t250390_x19():
    """State 0,1"""
    call = t250390_x18(z1=1103, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 2"""
        assert t250390_x1()
    elif call.Get() == 0:
        pass
    """State 3"""
    return 0

def t250390_x20():
    """State 0,2"""
    call = t250390_x18(z1=1102, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t250390_x21():
    """State 0,1"""
    assert t250390_x18(z1=1001, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t250390_x22(val2=10, val3=12):
    """State 0"""
    while True:
        """State 1"""
        call = t250390_x15(val2=val2, val3=val3)
        if f122() == 1:
            break
        elif not f122():
            """State 3"""
            call = t250390_x25(val2=val2, val3=val3)
            assert not IsPlayerDead()
    """State 2"""
    t250390_x12(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t250390_x23():
    """State 0,1"""
    assert t250390_x18(z1=1100, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t250390_x24(actionbutton1=7003900, flag5=1775, flag6=6001, val6=1000000, val7=1000000, val8=1000000,
                val9=1000000, val10=1000000):
    """State 0,1"""
    call = t250390_x18(z1=2000, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 2"""
        assert (t250390_x0(actionbutton1=actionbutton1, flag6=flag6, flag10=6000, flag11=6000, flag12=6000,
                flag13=6000, actionbutton2=0, flag5=flag5, val6=val6, val7=val7, val8=val8, val9=val9,
                val10=val10))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t250390_x25(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 3"""
    call = t250390_x26()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 2"""
        assert t250390_x1()
    """State 4"""
    return 0

def t250390_x26():
    """State 0,1"""
    assert t250390_x18(z1=1002, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t250390_x27(actionbutton1=7003900, flag6=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
                actionbutton2=0, flag5=_):
    """State 0"""
    while Loop('mainloop'):
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventStatus(flag6) == 1 or GetEventStatus(flag10) == 1 or GetEventStatus(flag11) ==
                1 or GetEventStatus(flag12) == 1 or GetEventStatus(flag13) == 1)
        while True:
            """State 4"""
            assert not GetEventStatus(flag5)
            """State 2"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                Continue('mainloop')
            elif (not GetEventStatus(flag6) and not GetEventStatus(flag10) and not GetEventStatus(flag11)
                  and not GetEventStatus(flag12) and not GetEventStatus(flag13)):
                Continue('mainloop')
            elif GetEventStatus(flag5) == 1:
                pass
            elif CheckActionButtonArea(actionbutton1 + actionbutton2) and not f116(10000) == 90:
                Break('mainloop')
    """State 5"""
    SetTalkTime(0.1)
    return 0

def t250390_x28():
    """State 0,1"""
    if not GetEventStatus(72500152):
        """State 2"""
        # talk:39060000:"Excuse me, young man..."
        assert t250390_x3(text3=39060000, z3=72500152, flag16=1, mode13=1)
    else:
        """State 3"""
        # talk:39060010:"Young man, excuse me..."
        assert t250390_x3(text3=39060010, z3=72500154, flag16=1, mode13=1)
    """State 4"""
    return 0

