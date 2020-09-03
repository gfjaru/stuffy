nState = 0
return
NumpadDiv::
	nState := !nState ;; toggle nState
return

;; Check nState is on or off, so this not fully disable the numeric pad
#If nState=1
	Numpad1::
		Send, {F13}
	return

	Numpad2::
		Send, {F14}
	return

	Numpad3::
		Send, {F15}
	return

	Numpad4::
		Send, {F16}
	return

	Numpad5::
		Send, {F17}
	return

	Numpad6::
		Send, {F18}
	return

	Numpad7::
		Send, {F19}
	return

	Numpad8::
		Send, {F20}
	return

	Numpad9::
		Send, {F21}
	return

	Numpad0::
		Send, {F22}
	return

	NumpadDot::
		Send, {F23}
	return

	NumpadAdd::
		Send, {Volume_Up}
	return
	
	NumpadSub::
		Send, {Volume_Down}
	return

	NumpadMult::
		Send, {Volume_Mute}
	return
#if