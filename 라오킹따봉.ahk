#SingleInstance, force
#NoEnv
  
;------------------------------------------------------set gui
Gui, Add, text, x30 y5 w110 h20, 악수 대신 해드려요
Gui, Add, text, x60 y25 w50 h20 vA, 준비
Gui, Add, button, x20 y50 w110 h20, 시작
Gui, Add, button, x20 y80 w110 h20, 중지
Gui, Add, button, x20 y110 w110 h20, 종료

Gui, Show,, 쉽게 악수를 눌러 보아요
Return
;-----------------------------------------------------set end

Button시작:
{
    CoordMode, Mouse, windows
    매크로시작:=1
    Loop
    {
        Gui,Submit,NoHide
        GuiControl, , A, 시작1

        ImageSearch, vx, vy, 950, 400, 1100, 500,*50 a.png
        If(ErrorLevel=0)
        {
            Sleep, 500
            Mouseclick, left, vx, vy
        }

        Sleep,500
        Gui,Submit,NoHide
        GuiControl, , A, 시작22
        
        If(매크로시작=2)
        {
            break
        }

        Sleep,500
        Gui,Submit,NoHide
        GuiControl, , A, 시작333

        If(매크로시작=3)
        {
            break
        }

    }   
}
Return

Button중지:
{
    Gui,Submit,NoHide
    GuiControl, , A, 중지
    CoordMode, Mouse, windows
    매크로시작 :=2
}
Return

Button종료:
{
    매크로시작 :=3
    ExitApp
}
Return