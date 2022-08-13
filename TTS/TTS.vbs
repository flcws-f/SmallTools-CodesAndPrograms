dim say
dim WSHShell
set WSHShell=wscript.createobject("wscript.shell")
while True
If say="C" Then
WSHShell.run "taskkill /im wscript.exe /f",0,true
end if
say=Inputbox("Input sentences(Input C to cancel)","TTS")
CreateObject("SAPI.SpVoice").Speak say
wend