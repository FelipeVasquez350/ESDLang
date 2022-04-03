# -*- coding: utf-8 -*-
def t110192_1():
    """State 0,1"""
    t110192_x4(flag1=70009029, flag2=70009025, flag3=70009026, val1=5, val2=10, val3=12, val4=10, val5=12,
               flag4=6001, actionbutton1=7001902, flag5=6000, flag6=6001, flag7=6000, flag8=6000, z1=1,
               val6=1000000, val7=1000000, val8=1000000)
    Quit()

def t110192_1000():
    """State 0,1,2,4"""
    # talk:19000200:"Hot... So hot... "
    assert t110192_x3(text1=19000200, flag9=0, mode5=1)
    """State 3"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t110192_x0(actionbutton1=7001902, flag6=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
               actionbutton2=0, flag5=6000):
    """State 0"""
    while Loop('mainloop'):
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 3"""
        assert (GetEventStatus(flag6) == 1 or GetEventStatus(flag10) == 1 or GetEventStatus(flag11) ==
                1 or GetEventStatus(flag12) == 1 or GetEventStatus(flag13) == 1)
        while True:
            """State 4"""
            assert not GetEventStatus(flag5)
            """State 2"""
            if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())):
                Continue('mainloop')
            elif (not GetEventStatus(flag6) and not GetEventStatus(flag10) and not GetEventStatus(flag11)
                  and not GetEventStatus(flag12) and not GetEventStatus(flag13)):
                Continue('mainloop')
            elif GetEventStatus(flag5) == 1:
                pass
            elif CheckActionButtonArea(actionbutton1 + actionbutton2):
                Break('mainloop')
    """State 5"""
    SetTalkTime(0.1)
    return 0

def t110192_x1():
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

def t110192_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t110192_x3(text1=19000200, flag9=0, mode5=1):
    """State 0,6"""
    assert t110192_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not flag9:
        """State 1"""
        # talk:19000200:"Hot... So hot... "
        TalkToPlayer(text1, -1, -1, flag9, 0)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        # talk:19000200:"Hot... So hot... "
        TalkToPlayer(text1, -1, -1, flag9, 1)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 7"""
    return 0

def t110192_x4(flag1=70009029, flag2=70009025, flag3=70009026, val1=5, val2=10, val3=12, val4=10, val5=12,
               flag4=6001, actionbutton1=7001902, flag5=6000, flag6=6001, flag7=6000, flag8=6000, z1=1,
               val6=1000000, val7=1000000, val8=1000000):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t110192_x5(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, flag4=flag4, actionbutton1=actionbutton1,
                          flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, val6=val6, val7=val7,
                          val8=val8)
        def WhilePaused():
            c5_116(GetDistanceToPlayer() < 4)
        if CheckSelfDeath() == 1 or GetEventStatus(flag1) == 1:
            pass
        elif GetEventStatus(flag2) == 1 or GetEventStatus(flag3) == 1:
            """State 3"""
            call = t110192_x20(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventStatus(flag1) == 1 or DoesSelfHaveSpEffect(30100) == 1:
                pass
            elif not GetEventStatus(flag2) and not GetEventStatus(flag3):
                continue
        """State 2"""
        call = t110192_x6(flag1=flag1, val2=val2, val3=val3)
        assert not CheckSelfDeath() and not GetEventStatus(flag1) and not DoesSelfHaveSpEffect(30100)
    """Unused"""
    """State 4"""
    return 0

def t110192_x5(val1=5, val2=10, val3=12, val4=10, val5=12, flag4=6001, actionbutton1=7001902, flag5=6000,
               flag6=6001, flag7=6000, flag8=6000, z1=1, val6=1000000, val7=1000000, val8=1000000):
    """State 0"""
    while True:
        """State 4"""
        call = t110192_x22(actionbutton1=actionbutton1, flag5=flag5, flag6=flag6, val6=val6, val7=val7,
                           val8=val8)
        if call.Done():
            """State 1"""
            Label('L0')
            call = t110192_x7(val1=val1, z1=z1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1:
            pass
        elif GetEventStatus(flag8) == 1:
            Goto('L0')
        elif not GetEventStatus(flag4) and GetEventStatus(flag7) == 1 and GetDistanceToPlayer() < val4:
            """State 3"""
            call = t110192_x8(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        """State 2"""
        def ExitPause():
            RemoveMyAggro()
        assert t110192_x9(val2=val2, val3=val3)
    """Unused"""
    """State 5"""
    return 0

def t110192_x6(flag1=70009029, val2=10, val3=12):
    """State 0,1"""
    if GetEventStatus(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t110192_x17()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3:
                """State 7"""
                assert t110192_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t110192_x7(val1=5, z1=1):
    """State 0,2"""
    ClearPlayerDamageInfo()
    TurnCharacterToFaceEntity(-1, 10000, -1)
    call = t110192_x15()
    def WhilePaused():
        c1_117(z1, 10000)
        SetTalkTime(0.01)
        c1_120(1, 0, 9, 9, 9, 9, 9, 9, 9)
    if call.Done():
        pass
    elif HasPlayerBeenAttacked() == 1 or (GetTalkInterruptReason() == 5 and IsTalkInProgress() == 1):
        """State 1"""
        assert t110192_x12()
    elif GetDistanceToPlayer() > val1:
        """State 3"""
        assert t110192_x11()
    """State 4"""
    return 0

def t110192_x8(val5=12):
    """State 0,1"""
    call = t110192_x21()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5:
        """State 2"""
        assert t110192_x1()
    """State 3"""
    return 0

def t110192_x9(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 4"""
    assert t110192_x1()
    """State 1"""
    if GetDistanceToPlayer() < 10:
        """State 2,6"""
        call = t110192_x14()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 5"""
            assert t110192_x1()
    else:
        """State 3"""
        pass
    """State 7"""
    return 0

def t110192_x10(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 2"""
    call = t110192_x19()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 3"""
        assert t110192_x1()
    """State 4"""
    return 0

def t110192_x11():
    """State 0,1"""
    assert t110192_x1()
    """State 2"""
    return 0

def t110192_x12():
    """State 0,2"""
    assert t110192_x1()
    """State 1"""
    ClearTalkProgressData()
    """State 3"""
    return 0

def t110192_x13(val2=10, val3=12):
    """State 0,2,1"""
    assert GetDistanceToPlayer() < val2
    """State 3"""
    call = t110192_x18()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 4"""
        assert t110192_x1()
    """State 5"""
    return 0

def t110192_x14():
    """State 0,1"""
    assert t110192_x16(z2=1101, mode1=0, mode2=0, mode3=0, mode4=0)
    """State 2"""
    return 0

def t110192_x15():
    """State 0,2"""
    assert f116(10000) == 1
    """State 1"""
    assert GetCurrentStateElapsedTime() > 0.6
    """State 3"""
    assert t110192_x16(z2=1000, mode1=0, mode2=0, mode3=0, mode4=0)
    """State 4"""
    return 0

def t110192_x16(z2=_, mode1=0, mode2=0, mode3=0, mode4=0):
    """State 0,4"""
    if f118(z2) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 1"""
        def WhilePaused():
            c1_118(z2)
        assert f117() == mode1 or f117() == mode2 or f117() == mode3 or f117() == mode4
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t110192_x17():
    """State 0,1"""
    call = t110192_x16(z2=1103, mode1=0, mode2=0, mode3=0, mode4=0)
    if call.Get() == 1:
        """State 2"""
        assert t110192_x1()
    elif call.Get() == 0:
        pass
    """State 3"""
    return 0

def t110192_x18():
    """State 0,2"""
    call = t110192_x16(z2=1102, mode1=0, mode2=0, mode3=0, mode4=0)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t110192_x19():
    """State 0,1"""
    assert t110192_x16(z2=1001, mode1=0, mode2=0, mode3=0, mode4=0)
    """State 2"""
    return 0

def t110192_x20(val2=10, val3=12):
    """State 0"""
    while True:
        """State 1"""
        call = t110192_x13(val2=val2, val3=val3)
        if f122() == 1:
            break
        elif not f122():
            """State 3"""
            call = t110192_x23(val2=val2, val3=val3)
            assert not IsPlayerDead()
    """State 2"""
    t110192_x10(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t110192_x21():
    """State 0,1"""
    assert t110192_x16(z2=1100, mode1=0, mode2=0, mode3=0, mode4=0)
    """State 2"""
    return 0

def t110192_x22(actionbutton1=7001902, flag5=6000, flag6=6001, val6=1000000, val7=1000000, val8=1000000):
    """State 0,3"""
    call = t110192_x16(z2=2000, mode1=0, mode2=0, mode3=0, mode4=0)
    if call.Get() == 1:
        while Loop('mainloop'):
            """State 4"""
            call = t110192_x0(actionbutton1=actionbutton1, flag6=flag6, flag10=6000, flag11=6000, flag12=6000,
                              flag13=6000, actionbutton2=0, flag5=flag5)
            if call.Done():
                break
            elif not f116(-1) == val6 and not f116(-1) == val7 and not f116(-1) == val8 and not DoesSelfHaveSpEffect(4510):
                while True:
                    """State 1"""
                    assert (f116(-1) == val6 or f116(-1) == val7 or f116(-1) == val8 or DoesSelfHaveSpEffect(4510)
                            == 1)
                    """State 2"""
                    if GetCurrentStateElapsedTime() > 1:
                        Continue('mainloop')
                    elif (f116(-1) == val6 and f116(-1) == val7 and f116(-1) == val8 and DoesSelfHaveSpEffect(4510)
                          == 1):
                        pass
    elif call.Done():
        pass
    """State 5"""
    return 0

def t110192_x23(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 3"""
    call = t110192_x24()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 2"""
        assert t110192_x1()
    """State 4"""
    return 0

def t110192_x24():
    """State 0,1"""
    assert t110192_x16(z2=1002, mode1=0, mode2=0, mode3=0, mode4=0)
    """State 2"""
    return 0

