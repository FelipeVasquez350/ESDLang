# -*- coding: utf-8 -*-
def t100210_1():
    """State 0"""
    while True:
        """State 1"""
        call = t100210_x6(flag5=1519, flag6=1515, flag7=1501, val1=5, val2=30, val3=40, val4=10, val5=12,
                          flag8=6001, actionbutton1=7002100, flag9=6000, flag10=6001, flag11=6000, flag12=6000,
                          mode1=1, val6=1000000, val7=1000000, val8=1000000, mode2=1, mode3=1, mode4=0,
                          val9=1000000, val10=1000000, mode5=0, flag13=6000, mode6=0)
        assert GetEventStatus(8304) == 1
        """State 2"""
        call = t100210_x1()
        assert not GetEventStatus(8304)

def t100210_1000():
    """State 0,6"""
    assert f116(-1) == 1000000
    """State 2"""
    if GetEventStatus(1502) == 1:
        """State 4"""
        if GetEventStatus(71000350) == 1:
            """State 8"""
            # talk:21000100:"(Panting)"
            assert t100210_x5(text5=21000100, flag18=0, mode11=1)
        else:
            """State 5,9"""
            # talk:21000200:"Hmm..."
            assert t100210_x5(text5=21000200, flag18=0, mode11=1)
    else:
        """State 3,7"""
        # talk:21000000:"You've done well to come this far. "
        assert t100210_x4(text6=21000000, z2=71000350, flag19=0, mode12=1)
    """State 1"""
    c1_119(0)
    Quit()

def t100210_1101():
    """State 0,2"""
    if IsPlayerAttacking() == 1:
        """State 4,5"""
        # talk:21030000:"What are you doing?!", talk:21030010:"Stop!"
        assert (t100210_x28(text1=21030000, flag1=71000396, text2=21030010, flag2=71000397, text3=-1,
                flag3=71000398, text4=-1, flag4=71000399))
    else:
        """State 3"""
        pass
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t100210_1102():
    """State 0,3"""
    if GetEventStatus(1515) == 1:
        pass
    else:
        while True:
            """State 4"""
            if not GetEventStatus(71000351) and GetEventStatus(71000389) == 1:
                """State 6"""
                # talk:21000010:"   "
                assert t100210_x3(text1=21000010, flag1=71000351, flag20=1, mode13=1)
            elif GetEventStatus(71000390) == 1 and not GetEventStatus(71000352):
                """State 7"""
                # talk:21060100:"Hear me! My name is Nogami Gensai!"
                def ExitPause():
                    SetEventState(71000352, 1)
                assert t100210_x5(text5=21060100, flag18=1, mode11=1)
    while True:
        """State 2"""
        assert not GetEventStatus(71000391)
        """State 5"""
        # talk:21030100:"Nothing but a rogue after all!"
        assert t100210_x3(text1=21030100, flag1=71000391, flag20=1, mode13=1)
    """Unused"""
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t100210_1103():
    """State 0,2"""
    if GetEventStatus(1515) == 1 or GetEventStatus(1516) == 1:
        """State 3,5"""
        # talk:21030200:"You...bastard..."
        assert t100210_x5(text5=21030200, flag18=1, mode11=1)
    else:
        """State 4,6"""
        # talk:21060200:"I...I've failed..."
        assert t100210_x5(text5=21060200, flag18=1, mode11=1)
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t100210_2000():
    """State 0,3"""
    assert (t100210_x0(actionbutton1=7002100, flag10=6001, flag14=6000, flag15=6000, flag16=6000, flag17=6000,
            actionbutton2=0, flag9=6000, val6=1000000, val7=1000000, val8=1000000, val9=1000000, val10=1000000))
    """State 2"""
    SetEventStateIf(GetEventStatus(1502) == 1, 71000388, 1)
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t100210_x0(actionbutton1=7002100, flag10=6001, flag14=6000, flag15=6000, flag16=6000, flag17=6000,
               actionbutton2=0, flag9=6000, val6=1000000, val7=1000000, val8=1000000, val9=1000000, val10=1000000):
    """State 0"""
    while Loop('mainloop'):
        """State 3"""
        call = t100210_x27(actionbutton1=actionbutton1, flag10=flag10, flag14=flag14, flag15=flag15,
                           flag16=flag16, flag17=flag17, actionbutton2=actionbutton2, flag9=flag9)
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

def t100210_x1():
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

def t100210_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t100210_x3(text1=_, flag1=_, flag20=1, mode13=1):
    """State 0,7"""
    assert t100210_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(flag1, 1)
    """State 6"""
    if not flag20:
        """State 1"""
        TalkToPlayer(text1, -1, -1, flag20, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        TalkToPlayer(text1, -1, -1, flag20, 1)
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

def t100210_x4(text6=21000000, z2=71000350, flag19=0, mode12=1):
    """State 0,7"""
    assert t100210_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 5"""
    if not flag19:
        """State 1"""
        # talk:21000000:"You've done well to come this far. "
        TalkToPlayer(text6, -1, -1, flag19, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 6"""
        # talk:21000000:"You've done well to come this far. "
        TalkToPlayer(text6, -1, -1, flag19, 1)
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

def t100210_x5(text5=_, flag18=_, mode11=1):
    """State 0,6"""
    assert t100210_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not flag18:
        """State 1"""
        TalkToPlayer(text5, -1, -1, flag18, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        TalkToPlayer(text5, -1, -1, flag18, 1)
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

def t100210_x6(flag5=1519, flag6=1515, flag7=1501, val1=5, val2=30, val3=40, val4=10, val5=12, flag8=6001,
               actionbutton1=7002100, flag9=6000, flag10=6001, flag11=6000, flag12=6000, mode1=1, val6=1000000,
               val7=1000000, val8=1000000, mode2=1, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0,
               flag13=6000, mode6=0):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t100210_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, flag8=flag8, actionbutton1=actionbutton1,
                          flag9=flag9, flag10=flag10, flag11=flag11, flag12=flag12, mode1=mode1, val6=val6,
                          val7=val7, val8=val8, mode2=mode2, mode3=mode3, mode4=mode4, val9=val9, val10=val10,
                          mode5=mode5, mode6=mode6)
        def WhilePaused():
            c5_116(GetDistanceToPlayer() < 4)
        if (CheckSelfDeath() == 1 or GetEventStatus(flag5) == 1) and not GetEventStatus(flag13):
            pass
        elif GetEventStatus(flag6) == 1 or GetEventStatus(flag7) == 1:
            """State 3"""
            call = t100210_x22(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventStatus(flag5) == 1 or DoesSelfHaveSpEffect(30100) == 1:
                pass
            elif not GetEventStatus(flag6) and not GetEventStatus(flag7):
                continue
        """State 2"""
        call = t100210_x8(flag5=flag5, val2=val2, val3=val3)
        assert not CheckSelfDeath() and not GetEventStatus(flag5) and not DoesSelfHaveSpEffect(30100)
    """Unused"""
    """State 4"""
    return 0

def t100210_x7(val1=5, val2=30, val3=40, val4=10, val5=12, flag8=6001, actionbutton1=7002100, flag9=6000,
               flag10=6001, flag11=6000, flag12=6000, mode1=1, val6=1000000, val7=1000000, val8=1000000,
               mode2=1, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0, mode6=0):
    """State 0"""
    while True:
        """State 4"""
        call = t100210_x24(actionbutton1=actionbutton1, flag9=flag9, flag10=flag10, val6=val6, val7=val7,
                           val8=val8, val9=val9, val10=val10)
        if call.Done():
            """State 1"""
            Label('L0')
            call = t100210_x9(val1=val1, mode1=mode1, mode2=mode2, mode3=mode3, mode4=mode4, mode5=mode5)
            def WhilePaused():
                GiveSpEffectToPlayer(30700)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
                pass
        elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
            pass
        elif GetEventStatus(flag12) == 1:
            Goto('L0')
        elif not GetEventStatus(flag8) and GetEventStatus(flag11) == 1 and GetDistanceToPlayer() < val4:
            """State 3"""
            call = t100210_x10(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
                pass
        """State 2"""
        def ExitPause():
            RemoveMyAggro()
        assert t100210_x11(val2=val2, val3=val3)
    """Unused"""
    """State 5"""
    return 0

def t100210_x8(flag5=1519, val2=30, val3=40):
    """State 0,1"""
    if GetEventStatus(flag5) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t100210_x19()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3:
                """State 7"""
                assert t100210_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t100210_x9(val1=5, mode1=1, mode2=1, mode3=1, mode4=0, mode5=0):
    """State 0,2"""
    ClearPlayerDamageInfo()
    TurnCharacterToFaceEntity(-1, 10000, -1)
    call = t100210_x17(mode2=mode2, mode4=mode4)
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
        assert t100210_x14()
    elif GetDistanceToPlayer() > val1:
        """State 3"""
        assert t100210_x13()
    """State 4"""
    return 0

def t100210_x10(val5=12):
    """State 0,1"""
    call = t100210_x23()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5:
        """State 2"""
        assert t100210_x1()
    """State 3"""
    return 0

def t100210_x11(val2=30, val3=40):
    """State 0,4"""
    assert t100210_x1() and GetCurrentStateElapsedFrames() > 2
    """State 1"""
    if GetDistanceToPlayer() < 10:
        """State 2,6"""
        call = t100210_x16()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 5"""
            assert t100210_x1()
    else:
        """State 3"""
        pass
    """State 7"""
    return 0

def t100210_x12(val2=30, val3=40):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 2"""
    call = t100210_x21()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 3"""
        assert t100210_x1()
    """State 4"""
    return 0

def t100210_x13():
    """State 0,1"""
    assert t100210_x1()
    """State 2"""
    return 0

def t100210_x14():
    """State 0,2"""
    assert t100210_x1()
    """State 1"""
    ClearTalkProgressData()
    """State 3"""
    return 0

def t100210_x15(val2=30, val3=40):
    """State 0,2"""
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t100210_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3:
            """State 4"""
            assert t100210_x1()
    """Unused"""
    """State 5"""
    return 0

def t100210_x16():
    """State 0,1"""
    assert t100210_x18(z1=1101, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t100210_x17(mode2=1, mode4=0):
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
        assert t100210_x18(z1=1000, mode7=0, mode8=0, mode9=0, mode10=0)
    elif GetCurrentStateElapsedTime() > 5:
        pass
    """State 5"""
    return 0

def t100210_x18(z1=_, mode7=0, mode8=0, mode9=0, mode10=0):
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

def t100210_x19():
    """State 0,1"""
    call = t100210_x18(z1=1103, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 2"""
        assert t100210_x1()
    elif call.Get() == 0:
        pass
    """State 3"""
    return 0

def t100210_x20():
    """State 0,2"""
    call = t100210_x18(z1=1102, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t100210_x21():
    """State 0,1"""
    assert t100210_x18(z1=1001, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t100210_x22(val2=30, val3=40):
    """State 0"""
    while True:
        """State 1"""
        call = t100210_x15(val2=val2, val3=val3)
        if f122() == 1:
            break
        elif not f122():
            """State 3"""
            call = t100210_x25(val2=val2, val3=val3)
            assert not IsPlayerDead()
    """State 2"""
    t100210_x12(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t100210_x23():
    """State 0,1"""
    assert t100210_x18(z1=1100, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t100210_x24(actionbutton1=7002100, flag9=6000, flag10=6001, val6=1000000, val7=1000000, val8=1000000,
                val9=1000000, val10=1000000):
    """State 0,1"""
    call = t100210_x18(z1=2000, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 2"""
        assert (t100210_x0(actionbutton1=actionbutton1, flag10=flag10, flag14=6000, flag15=6000, flag16=6000,
                flag17=6000, actionbutton2=0, flag9=flag9, val6=val6, val7=val7, val8=val8, val9=val9,
                val10=val10))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t100210_x25(val2=30, val3=40):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 3"""
    call = t100210_x26()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 2"""
        assert t100210_x1()
    """State 4"""
    return 0

def t100210_x26():
    """State 0,1"""
    assert t100210_x18(z1=1002, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t100210_x27(actionbutton1=7002100, flag10=6001, flag14=6000, flag15=6000, flag16=6000, flag17=6000,
                actionbutton2=0, flag9=6000):
    """State 0"""
    while Loop('mainloop'):
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventStatus(flag10) == 1 or GetEventStatus(flag14) == 1 or GetEventStatus(flag15)
                == 1 or GetEventStatus(flag16) == 1 or GetEventStatus(flag17) == 1)
        while True:
            """State 4"""
            assert not GetEventStatus(flag9)
            """State 2"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                Continue('mainloop')
            elif (not GetEventStatus(flag10) and not GetEventStatus(flag14) and not GetEventStatus(flag15)
                  and not GetEventStatus(flag16) and not GetEventStatus(flag17)):
                Continue('mainloop')
            elif GetEventStatus(flag9) == 1:
                pass
            elif CheckActionButtonArea(actionbutton1 + actionbutton2) and not f116(10000) == 90:
                Break('mainloop')
    """State 5"""
    SetTalkTime(0.1)
    return 0

def t100210_x28(text1=21030000, flag1=71000396, text2=21030010, flag2=71000397, text3=-1, flag3=71000398,
                text4=-1, flag4=71000399):
    """State 0,3"""
    if ((text1 == -1 or GetEventStatus(flag1) == 1) and (text2 == -1 or GetEventStatus(flag2) == 1) and
        (text3 == -1 or GetEventStatus(flag3) == 1) and (text4 == -1 or GetEventStatus(flag4) == 1)):
        """State 2"""
        SetEventState(flag1, 0)
        SetEventState(flag2, 0)
        SetEventState(flag3, 0)
        SetEventState(flag4, 0)
    else:
        pass
    """State 1"""
    if not text1 == -1 and not GetEventStatus(flag1):
        """State 4"""
        assert t100210_x3(text1=text1, flag1=flag1, flag20=1, mode13=1)
    elif not text2 == -1 and not GetEventStatus(flag2):
        """State 5"""
        assert t100210_x3(text1=text2, flag1=flag2, flag20=1, mode13=1)
    elif not text3 == -1 and not GetEventStatus(flag3):
        """State 6"""
        assert t100210_x3(text1=text3, flag1=flag3, flag20=1, mode13=1)
    else:
        """State 7"""
        assert t100210_x3(text1=text4, flag1=flag4, flag20=1, mode13=1)
    """State 8"""
    return 0

