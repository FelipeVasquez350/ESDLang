# -*- coding: utf-8 -*-
def t130300_1():
    """State 0,1"""
    t130300_x7(flag9=1439, flag10=1435, flag11=1436, val1=5, val2=10, val3=12, val4=10, val5=12, flag12=6001,
               actionbutton1=7003000, flag13=6000, flag14=6001, flag15=6000, flag16=6000, mode1=1, val6=1000000,
               val7=1000000, val8=1000000, mode2=0, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0,
               flag17=6000, mode6=0)
    Quit()

def t130300_1000():
    """State 0,2"""
    if GetEventStatus(1426) == 1:
        """State 3"""
        # talk:30900000:"(Wheeze... wheeze... wheeze...)", talk:30900100:"(Wheeze... wheeze... wheeze...)", talk:30900150:"Right...", talk:30910050:"(Pant... pant... pant...)", talk:30910200:"I'm taking a blood sample.", talk:30910210:"... Now to bring this to Lady Emma.", talk:30910100:".........", talk:30910000:"Drink this...", talk:30900200:"I can breathe easier now that the sickness is gone.", goods:9504:Rot Essence: Charmed One
        call = t130300_x29(text5=30900000, text6=30900100, text7=30900150, text8=30910050, text9=30910200,
                           text10=30910210, text11=30910100, text12=30910000, text13=30900200, flag5=70002030,
                           flag6=71120184, flag7=71120182, flag8=71120185, z1=71120181, z2=71120180,
                           z3=71120183, z4=71120186, goods1=9504)
        def WhilePaused():
            c1_120(1, 10, 9, 9, 9, 9, 9, 9, 9)
            c1_117(1102001, -1)
        if call.Get() == 0:
            pass
        elif call.Done():
            """State 5"""
            assert t130300_x31()
    elif GetEventStatus(1424) == 1:
        """State 4"""
        def WhilePaused():
            c1_120(1, 10, 9, 9, 9, 9, 9, 9, 9)
        assert t130300_x32()
    else:
        pass
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t130300_1001():
    """State 0,2"""
    if True:
        """State 3"""
        # talk:30130100:"...no appreciation for her beauty!"
        assert t130300_x5(text5=30130100, flag22=1, mode11=1)
    elif GetEventStatus(11500690) == 1:
        pass
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t130300_1101():
    """State 0,4"""
    if GetEventStatus(1424) == 1:
        """State 3,8"""
        # talk:30200400:"(Sickly groans)"
        assert t130300_x5(text5=30200400, flag22=1, mode11=1)
    else:
        """State 5"""
        if GetEventStatus(11500690) == 1:
            pass
        else:
            """State 2"""
            if GetEventStatus(70002030) == 1:
                """State 7"""
                # talk:30030000:"   ", talk:30030100:"   "
                assert (t130300_x30(text1=30030000, flag1=71300003, text2=30030100, flag2=71300004, text3=-1,
                        flag3=71300005, text4=-1, flag4=71300006))
            else:
                """State 6"""
                # talk:30030000:"   ", talk:30030100:"   ", talk:30030200:"Ugh, would you stop that?!", talk:30030300:"Guh... Shinobi, what are you doing?!"
                assert (t130300_x30(text1=30030000, flag1=71300003, text2=30030100, flag2=71300004, text3=30030200,
                        flag3=71300005, text4=30030300, flag4=71300006))
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t130300_1102():
    """State 0"""
    while True:
        """State 2"""
        if GetEventStatus(11500690) == 1:
            break
        elif not GetEventStatus(71500194):
            """State 3,5"""
            # talk:30130000:"I see..."
            assert t130300_x3(text1=30130000, flag1=71500194, flag24=1, mode13=1)
    while True:
        """State 4"""
        assert GetEventStatus(71300007) == 1 and not GetEventStatus(71500194)
        """State 6"""
        # talk:30000550:"The melody.... Give it back!!"
        assert t130300_x3(text1=30000550, flag1=71500194, flag24=1, mode13=1)
    """Unused"""
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t130300_1103():
    """State 0,2"""
    if GetEventStatus(1424) == 1 or GetEventStatus(11500690) == 1:
        pass
    else:
        """State 3"""
        # talk:30130200:"Ahh..."
        assert t130300_x5(text5=30130200, flag22=1, mode11=1)
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t130300_2000():
    """State 0,2"""
    call = t130300_x34()
    if call.Done():
        pass
    else:
        """State 3"""
        assert (t130300_x0(actionbutton1=7003020, flag14=6001, flag18=6000, flag19=6000, flag20=6000,
                flag21=6000, actionbutton2=0, flag13=6000, val6=1000000, val7=1000000, val8=1000000,
                val9=-1, val10=-1))
    """State 1"""
    def WhilePaused():
        c1_119(0)
    Quit()

def t130300_x0(actionbutton1=_, flag14=6001, flag18=6000, flag19=6000, flag20=6000, flag21=6000, actionbutton2=0,
               flag13=6000, val6=1000000, val7=1000000, val8=1000000, val9=_, val10=_):
    """State 0"""
    while Loop('mainloop'):
        """State 3"""
        call = t130300_x28(actionbutton1=actionbutton1, flag14=flag14, flag18=flag18, flag19=flag19,
                           flag20=flag20, flag21=flag21, actionbutton2=actionbutton2, flag13=flag13)
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

def t130300_x1():
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

def t130300_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t130300_x3(text1=_, flag1=_, flag24=1, mode13=1):
    """State 0,7"""
    assert t130300_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(flag1, 1)
    """State 6"""
    if not flag24:
        """State 1"""
        TalkToPlayer(text1, -1, -1, flag24, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        TalkToPlayer(text1, -1, -1, flag24, 1)
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

def t130300_x4(text14=_, z6=_, flag23=0, mode12=1):
    """State 0,7"""
    assert t130300_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 5"""
    if not flag23:
        """State 1"""
        TalkToPlayer(text14, -1, -1, flag23, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 6"""
        TalkToPlayer(text14, -1, -1, flag23, 1)
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
    SetEventState(z6, 1)
    """State 8"""
    return 0

def t130300_x5(text5=_, flag22=_, mode11=1):
    """State 0,6"""
    assert t130300_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not flag22:
        """State 1"""
        TalkToPlayer(text5, -1, -1, flag22, 0)
        def WhilePaused():
            GiveSpEffectToPlayer(30700)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 5"""
        TalkToPlayer(text5, -1, -1, flag22, 1)
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

def t130300_x6(lot1=69900):
    """State 0,1"""
    GetItemFromItemLot(lot1)
    while True:
        """State 2"""
        assert not IsMenuOpen(63) and GetCurrentStateElapsedTime() > 0.01
        """State 3"""
        assert GetCurrentStateElapsedTime() > 0.01
        """State 4"""
        if not IsMenuOpen(63):
            break
        else:
            pass
    """State 5"""
    return 0

def t130300_x7(flag9=1439, flag10=1435, flag11=1436, val1=5, val2=10, val3=12, val4=10, val5=12, flag12=6001,
               actionbutton1=7003000, flag13=6000, flag14=6001, flag15=6000, flag16=6000, mode1=1, val6=1000000,
               val7=1000000, val8=1000000, mode2=0, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0,
               flag17=6000, mode6=0):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t130300_x8(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, flag12=flag12, actionbutton1=actionbutton1,
                          flag13=flag13, flag14=flag14, flag15=flag15, flag16=flag16, mode1=mode1, val6=val6,
                          val7=val7, val8=val8, mode2=mode2, mode3=mode3, mode4=mode4, val9=val9, val10=val10,
                          mode5=mode5, mode6=mode6)
        def WhilePaused():
            c5_116(GetDistanceToPlayer() < 4)
        if (CheckSelfDeath() == 1 or GetEventStatus(flag9) == 1) and not GetEventStatus(flag17):
            pass
        elif GetEventStatus(flag10) == 1 or GetEventStatus(flag11) == 1:
            """State 3"""
            call = t130300_x23(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventStatus(flag9) == 1 or DoesSelfHaveSpEffect(30100) == 1:
                pass
            elif not GetEventStatus(flag10) and not GetEventStatus(flag11):
                continue
        """State 2"""
        call = t130300_x9(flag9=flag9, val2=val2, val3=val3)
        assert not CheckSelfDeath() and not GetEventStatus(flag9) and not DoesSelfHaveSpEffect(30100)
    """Unused"""
    """State 4"""
    return 0

def t130300_x8(val1=5, val2=10, val3=12, val4=10, val5=12, flag12=6001, actionbutton1=7003000, flag13=6000,
               flag14=6001, flag15=6000, flag16=6000, mode1=1, val6=1000000, val7=1000000, val8=1000000,
               mode2=0, mode3=1, mode4=0, val9=1000000, val10=1000000, mode5=0, mode6=0):
    """State 0"""
    while True:
        """State 4"""
        call = t130300_x25(actionbutton1=actionbutton1, flag13=flag13, flag14=flag14, val6=val6, val7=val7,
                           val8=val8, val9=val9, val10=val10)
        if call.Done():
            """State 1"""
            Label('L0')
            call = t130300_x10(val1=val1, mode1=mode1, mode2=mode2, mode3=mode3, mode4=mode4, mode5=mode5)
            def WhilePaused():
                GiveSpEffectToPlayer(30700)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
                pass
        elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
            pass
        elif GetEventStatus(flag16) == 1:
            Goto('L0')
        elif not GetEventStatus(flag12) and GetEventStatus(flag15) == 1 and GetDistanceToPlayer() < val4:
            """State 3"""
            call = t130300_x11(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1 and not mode6 and not DoesSelfHaveSpEffect(30201):
                pass
        """State 2"""
        def ExitPause():
            RemoveMyAggro()
        assert t130300_x12(val2=val2, val3=val3)
    """Unused"""
    """State 5"""
    return 0

def t130300_x9(flag9=1439, val2=10, val3=12):
    """State 0,1"""
    if GetEventStatus(flag9) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t130300_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3:
                """State 7"""
                assert t130300_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t130300_x10(val1=5, mode1=1, mode2=0, mode3=1, mode4=0, mode5=0):
    """State 0,2"""
    ClearPlayerDamageInfo()
    TurnCharacterToFaceEntity(-1, 10000, -1)
    call = t130300_x18(mode2=mode2, mode4=mode4)
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
        assert t130300_x15()
    elif GetDistanceToPlayer() > val1:
        """State 3"""
        assert t130300_x14()
    """State 4"""
    return 0

def t130300_x11(val5=12):
    """State 0,1"""
    call = t130300_x24()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5:
        """State 2"""
        assert t130300_x1()
    """State 3"""
    return 0

def t130300_x12(val2=10, val3=12):
    """State 0,4"""
    assert t130300_x1() and GetCurrentStateElapsedFrames() > 2
    """State 1"""
    if GetDistanceToPlayer() < 10:
        """State 2,6"""
        call = t130300_x17()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 5"""
            assert t130300_x1()
    else:
        """State 3"""
        pass
    """State 7"""
    return 0

def t130300_x13(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 2"""
    call = t130300_x22()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 3"""
        assert t130300_x1()
    """State 4"""
    return 0

def t130300_x14():
    """State 0,1"""
    assert t130300_x1()
    """State 2"""
    return 0

def t130300_x15():
    """State 0,2"""
    assert t130300_x1()
    """State 1"""
    ClearTalkProgressData()
    """State 3"""
    return 0

def t130300_x16(val2=10, val3=12):
    """State 0,2"""
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t130300_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3:
            """State 4"""
            assert t130300_x1()
    """Unused"""
    """State 5"""
    return 0

def t130300_x17():
    """State 0,1"""
    assert t130300_x19(z5=1101, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t130300_x18(mode2=0, mode4=0):
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
        assert t130300_x19(z5=1000, mode7=0, mode8=0, mode9=0, mode10=0)
    elif GetCurrentStateElapsedTime() > 5:
        pass
    """State 5"""
    return 0

def t130300_x19(z5=_, mode7=0, mode8=0, mode9=0, mode10=0):
    """State 0,4"""
    if f118(z5) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 1"""
        def WhilePaused():
            c1_118(z5)
        assert f117() == mode7 or f117() == mode8 or f117() == mode9 or f117() == mode10
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t130300_x20():
    """State 0,1"""
    call = t130300_x19(z5=1103, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 2"""
        assert t130300_x1()
    elif call.Get() == 0:
        pass
    """State 3"""
    return 0

def t130300_x21():
    """State 0,2"""
    call = t130300_x19(z5=1102, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t130300_x22():
    """State 0,1"""
    assert t130300_x19(z5=1001, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t130300_x23(val2=10, val3=12):
    """State 0"""
    while True:
        """State 1"""
        call = t130300_x16(val2=val2, val3=val3)
        if f122() == 1:
            break
        elif not f122():
            """State 3"""
            call = t130300_x26(val2=val2, val3=val3)
            assert not IsPlayerDead()
    """State 2"""
    t130300_x13(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t130300_x24():
    """State 0,1"""
    assert t130300_x19(z5=1100, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t130300_x25(actionbutton1=7003000, flag13=6000, flag14=6001, val6=1000000, val7=1000000, val8=1000000,
                val9=1000000, val10=1000000):
    """State 0,1"""
    call = t130300_x19(z5=2000, mode7=0, mode8=0, mode9=0, mode10=0)
    if call.Get() == 1:
        """State 2"""
        assert (t130300_x0(actionbutton1=actionbutton1, flag14=flag14, flag18=6000, flag19=6000, flag20=6000,
                flag21=6000, actionbutton2=0, flag13=flag13, val6=val6, val7=val7, val8=val8, val9=val9,
                val10=val10))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t130300_x26(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 3"""
    call = t130300_x27()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3:
        """State 2"""
        assert t130300_x1()
    """State 4"""
    return 0

def t130300_x27():
    """State 0,1"""
    assert t130300_x19(z5=1002, mode7=0, mode8=0, mode9=0, mode10=0)
    """State 2"""
    return 0

def t130300_x28(actionbutton1=_, flag14=6001, flag18=6000, flag19=6000, flag20=6000, flag21=6000, actionbutton2=0,
                flag13=6000):
    """State 0"""
    while Loop('mainloop'):
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventStatus(flag14) == 1 or GetEventStatus(flag18) == 1 or GetEventStatus(flag19)
                == 1 or GetEventStatus(flag20) == 1 or GetEventStatus(flag21) == 1)
        while True:
            """State 4"""
            assert not GetEventStatus(flag13)
            """State 2"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                Continue('mainloop')
            elif (not GetEventStatus(flag14) and not GetEventStatus(flag18) and not GetEventStatus(flag19)
                  and not GetEventStatus(flag20) and not GetEventStatus(flag21)):
                Continue('mainloop')
            elif GetEventStatus(flag13) == 1:
                pass
            elif CheckActionButtonArea(actionbutton1 + actionbutton2) and not f116(10000) == 90:
                Break('mainloop')
    """State 5"""
    SetTalkTime(0.1)
    return 0

def t130300_x29(text5=30900000, text6=30900100, text7=30900150, text8=30910050, text9=30910200, text10=30910210,
                text11=30910100, text12=30910000, text13=30900200, flag5=70002030, flag6=71120184, flag7=71120182,
                flag8=71120185, z1=71120181, z2=71120180, z3=71120183, z4=71120186, goods1=9504):
    """State 0,43"""
    if GetEventStatus(flag7) == 1:
        """State 44"""
        if not GetEventStatus(50006990):
            """State 21"""
            Label('L0')
            """State 57"""
            assert t130300_x5(text5=text9, flag22=0, mode11=1)
            """State 48"""
            SetEventState(flag8, 1)
            """State 58"""
            assert t130300_x6(lot1=69900)
            """State 25"""
            Label('L1')
            """State 63"""
            assert t130300_x5(text5=text10, flag22=0, mode11=1)
            """State 23"""
            SetEventState(flag7, 0)
        else:
            """State 45,47"""
            if GetEventStatus(flag8) == 1:
                Goto('L1')
            else:
                """State 46,49"""
                SetEventState(flag7, 0)
                """State 1"""
                Label('L2')
                if GetEventStatus(flag5) == 1:
                    """State 2,12"""
                    if not GetEventStatus(flag6):
                        """State 50"""
                        if not GetEventStatus(70004000):
                            """State 3,55"""
                            assert t130300_x5(text5=text5, flag22=0, mode11=1)
                        else:
                            """State 4,56"""
                            assert t130300_x5(text5=text6, flag22=0, mode11=1)
                    else:
                        """State 52,64"""
                        assert t130300_x5(text5=text7, flag22=0, mode11=1)
                    """State 51"""
                    if not GetEventStatus(70004001):
                        """State 53,5"""
                        MainBonfireMenuFlag()
                        """State 6"""
                        ClearTalkListData()
                        """State 7"""
                        # action:14000003:"Do nothing"
                        AddTalkListData(2, 14000003, -1)
                        """State 8"""
                        OpenConversationChoicesMenu(0)
                        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                        """State 9,10"""
                    else:
                        """State 11"""
                        if not GetEventStatus(50006990):
                            """State 14,17"""
                            ClearTalkListData()
                            """State 18"""
                            # action:14000002:"Take coughed up blood sample"
                            AddTalkListData(1, 14000002, -1)
                            # action:14000003:"Do nothing"
                            AddTalkListData(2, 14000003, -1)
                            """State 19"""
                            OpenConversationChoicesMenu(0)
                            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                            """State 20"""
                            if GetTalkListEntryResult() == 1:
                                """State 24"""
                                SetEventState(flag7, 1)
                                Goto('L0')
                            else:
                                """State 22"""
                                pass
                        else:
                            """State 15"""
                            """State 13"""
                            pass
                else:
                    """State 39,40,66"""
                    return 1
    else:
        Goto('L2')
    """State 54"""
    Label('L3')
    SetEventState(flag6, 1)
    """State 65"""
    Label('L4')
    return 0
    """Unused"""
    """State 16,26"""
    ClearTalkListData()
    """State 27"""
    # action:14000000:"Give Dragonrot Pellet"
    AddTalkListDataIf(ComparePlayerInventoryNumber(3, 9550, 4, 1, 0) == 1, 1, 14000000, -1)
    # action:14000001:"Say nothing"
    AddTalkListData(2, 14000001, -1)
    """State 28"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 29"""
    if GetTalkListEntryResult() == 1:
        Goto('L10')
    elif GetTalkListEntryResult() == 2:
        Goto('L8')
    else:
        Goto('L4')
    """State 30"""
    Label('L5')
    Goto('L12')
    """State 31"""
    Label('L6')
    SetEventState(z2, 0)
    Goto('L3')
    """State 32"""
    Label('L7')
    SetEventState(z2, 1)
    Goto('L5')
    """State 33"""
    Label('L8')
    SetEventState(z1, 1)
    """State 34"""
    Goto('L13')
    """State 35"""
    Label('L9')
    SetEventState(z1, 0)
    Goto('L3')
    """State 36"""
    Label('L10')
    PlayerEquipmentQuantityChange(3, 9550, -1)
    # goods:9504:Rot Essence: Charmed One
    PlayerEquipmentQuantityChange(3, goods1, -1)
    """State 37"""
    SetEventState(z3, 1)
    Goto('L7')
    """State 38"""
    Goto('L14')
    """State 41"""
    Goto('L15')
    """State 42"""
    Label('L11')
    SetEventState(z4, 0)
    Goto('L4')
    """State 59"""
    Label('L12')
    assert t130300_x5(text5=text12, flag22=0, mode11=1)
    Goto('L6')
    """State 60"""
    Label('L13')
    assert t130300_x5(text5=text11, flag22=0, mode11=1)
    Goto('L9')
    """State 61"""
    Label('L14')
    assert t130300_x5(text5=text8, flag22=0, mode11=1)
    Goto('L4')
    """State 62"""
    Label('L15')
    assert t130300_x5(text5=text13, flag22=0, mode11=1)
    Goto('L11')

def t130300_x30(text1=30030000, flag1=71300003, text2=30030100, flag2=71300004, text3=_, flag3=71300005,
                text4=_, flag4=71300006):
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
        assert t130300_x3(text1=text1, flag1=flag1, flag24=1, mode13=1)
    elif not text2 == -1 and not GetEventStatus(flag2):
        """State 5"""
        assert t130300_x3(text1=text2, flag1=flag2, flag24=1, mode13=1)
    elif not text3 == -1 and not GetEventStatus(flag3):
        """State 6"""
        assert t130300_x3(text1=text3, flag1=flag3, flag24=1, mode13=1)
    else:
        """State 7"""
        assert t130300_x3(text1=text4, flag1=flag4, flag24=1, mode13=1)
    """State 8"""
    return 0

def t130300_x31():
    """State 0,29"""
    if GetEventStatus(11500690) == 1:
        """State 30,40"""
        # talk:30000500:"Why..."
        assert t130300_x4(text14=30000500, z6=71300007, flag23=0, mode12=1)
    else:
        """State 9"""
        if GetEventStatus(71300046) == 1:
            """State 27,38"""
            call = t130300_x33()
            if call.Get() == 0:
                pass
            elif call.Done():
                """State 28"""
                SetEventState(71300046, 0)
                """State 1"""
                Label('L0')
                if not GetEventStatus(71300001):
                    """State 2,31"""
                    # talk:30200000:"Ahhh... Ahhh..."
                    def WhilePaused():
                        c1_120(1, 10, 9, 9, 9, 9, 9, 9, 9)
                    assert t130300_x5(text5=30200000, flag22=0, mode11=1)
                    """State 3"""
                    ClearTalkListData()
                    """State 4"""
                    # action:14030000:"Greet him"
                    AddTalkListData(1, 14030000, -1)
                    # action:14030001:"Ignore him"
                    AddTalkListData(2, 14030001, -1)
                    """State 5"""
                    OpenConversationChoicesMenu(0)
                    def WhilePaused():
                        c1_120(1, 10, 9, 9, 9, 9, 9, 9, 9)
                    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                    """State 6"""
                    if GetTalkListEntryResult() == 1:
                        """State 8"""
                        SetEventState(71300044, 1)
                        """State 11"""
                        Label('L1')
                        """State 32"""
                        # talk:30210000:"Hey..."
                        def WhilePaused():
                            c1_120(1, 10, 9, 9, 9, 9, 9, 9, 9)
                        assert t130300_x4(text14=30210000, z6=71300001, flag23=0, mode12=1)
                        """State 13"""
                        SetEventState(71300044, 0)
                        Goto('L4')
                    elif GetTalkListEntryResult() == 2:
                        """State 7"""
                        SetEventState(71300045, 1)
                        """State 10"""
                        Label('L2')
                        """State 33"""
                        # talk:30210100:"........."
                        def WhilePaused():
                            c1_120(1, 10, 9, 9, 9, 9, 9, 9, 9)
                        assert t130300_x5(text5=30210100, flag22=0, mode11=1)
                        """State 12"""
                        SetEventState(71300045, 0)
                        Goto('L4')
                    else:
                        Goto('L4')
                else:
                    """State 14"""
                    if not GetEventStatus(71500192):
                        """State 15,34"""
                        # talk:30200100:"I must follow it."
                        def WhilePaused():
                            c1_120(1, 0, 9, 9, 9, 9, 9, 9, 9)
                        assert t130300_x5(text5=30200100, flag22=0, mode11=1)
                        """State 16"""
                        ClearTalkListData()
                        """State 35"""
                        call = t130300_x33()
                        if call.Get() == 0:
                            """State 17"""
                            # action:14030002:"Lure to Abandoned Dungeon"
                            AddTalkListData(1, 14030002, -1)
                            # action:14030004:"Don't mention Abandoned Dungeon"
                            AddTalkListData(2, 14030004, -1)
                        elif call.Done():
                            """State 18"""
                            # action:14030003:"I have not"
                            AddTalkListData(2, 14030003, -1)
                        """State 19"""
                        OpenConversationChoicesMenu(0)
                        def WhilePaused():
                            c1_120(1, 0, 9, 9, 9, 9, 9, 9, 9)
                        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                        """State 20"""
                        if GetTalkListEntryResult() == 1:
                            """State 22"""
                            SetEventState(71300046, 1)
                        elif GetTalkListEntryResult() == 2:
                            """State 21"""
                            SetEventState(71300047, 1)
                            """State 23"""
                            Label('L3')
                            """State 37"""
                            # talk:30210200:"Don't know."
                            def WhilePaused():
                                c1_120(1, 0, 9, 9, 9, 9, 9, 9, 9)
                            assert t130300_x5(text5=30210200, flag22=0, mode11=1)
                            """State 25"""
                            SetEventState(71300047, 0)
                            Goto('L4')
                        else:
                            Goto('L4')
                    else:
                        """State 39"""
                        # talk:30200200:"If I go to the abandoned dungeon, I can pursue the melody..."
                        def WhilePaused():
                            c1_120(1, 10, 9, 9, 9, 9, 9, 9, 9)
                        assert t130300_x5(text5=30200200, flag22=0, mode11=1)
                        Goto('L4')
        elif GetEventStatus(71300047) == 1:
            Goto('L3')
        elif GetEventStatus(71300044) == 1:
            Goto('L1')
        elif GetEventStatus(71300045) == 1:
            Goto('L2')
        else:
            Goto('L0')
        """State 24,36"""
        # talk:30210300:"Try the abandoned dungeon."
        def WhilePaused():
            c1_120(1, 0, 9, 9, 9, 9, 9, 9, 9)
        assert t130300_x4(text14=30210300, z6=71500192, flag23=0, mode12=1)
        """State 26"""
        SetEventState(71300046, 0)
    """State 41"""
    Label('L4')
    return 0

def t130300_x32():
    """State 0,1,2"""
    # talk:30200300:"(Sickly groaning)"
    assert t130300_x5(text5=30200300, flag22=0, mode11=1)
    """State 3"""
    return 0

def t130300_x33():
    """State 0,1"""
    if GetEventStatus(1479) == 1 or GetEventStatus(1475) == 1 or GetEventStatus(1476) == 1:
        pass
    else:
        """State 2"""
        if not GetEventStatus(71300050) or not GetEventStatus(1460):
            pass
        else:
            """State 3"""
            if not GetEventStatus(72009002):
                pass
            else:
                """State 4"""
                if GetEventStatus(1459) == 1 or GetEventStatus(1455) == 1 or GetEventStatus(1456) == 1:
                    pass
                else:
                    Goto('L0')
            """State 5"""
            return 0
    """State 6"""
    Label('L0')
    return 1

def t130300_x34():
    """State 0,1"""
    Label('L0')
    call = t130300_x0(actionbutton1=7003010, flag14=6001, flag18=6000, flag19=6000, flag20=6000, flag21=6000,
                      actionbutton2=0, flag13=6000, val6=1000000, val7=1000000, val8=1000000, val9=-1,
                      val10=-1)
    if call.Done():
        pass
    elif GetEventStatus(70002030) == 1:
        """State 3"""
        Label('L1')
        call = t130300_x0(actionbutton1=7003050, flag14=6001, flag18=6000, flag19=6000, flag20=6000,
                          flag21=6000, actionbutton2=0, flag13=6000, val6=1000000, val7=1000000, val8=1000000,
                          val9=-1, val10=-1)
        if call.Done():
            pass
        elif not GetEventStatus(70002030) and DoesPlayerHaveSpEffect(5450) == 1:
            """State 2"""
            Label('L2')
            call = t130300_x0(actionbutton1=7003011, flag14=6001, flag18=6000, flag19=6000, flag20=6000,
                              flag21=6000, actionbutton2=0, flag13=6000, val6=1000000, val7=1000000,
                              val8=1000000, val9=-1, val10=-1)
            if call.Done():
                pass
            elif GetEventStatus(70002030) == 1:
                Goto('L1')
            elif not DoesPlayerHaveSpEffect(5450):
                Goto('L0')
        elif not GetEventStatus(70002030) and not DoesPlayerHaveSpEffect(5450):
            Goto('L0')
    elif DoesPlayerHaveSpEffect(5450) == 1:
        Goto('L2')
    """State 4"""
    return 0

