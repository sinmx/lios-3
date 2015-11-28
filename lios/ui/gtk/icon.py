import gettext
gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext

stock_icon_dict = { _("File") :"edit-copy",
					_("New") :"gtk-new",
					_("Open"):"gtk-open",
					_("Save"):"gtk-save",
					_("Save-As"):"gtk-save-as",
					_("Find"):"gtk-find",
					_("Find-Replace"):"gtk-find-and-replace",
					_("Spell-Check"):"gtk-spell-check",
					_("Read"):"media-playback-start",
					_("Stop"):"media-playback-stop",
					_("Go-To-Page"):"go-jump",
					_("Go-To-Line"):"go-jump",
					_("Undo"):"edit-undo",
					_("Redo"):"edit-redo",
					_("Delete"):"gtk-remove",
					_("Punch-Text"):"insert-text",
					_("Append-Text"):"insert-text",
					_("Zoom-In"):"gtk-zoom-in",
					_("Zoom-Fit"):"gtk-zoom-fit",
					_("Zoom-Out"):"gtk-zoom-out",
					_("Rotate-Left"):"object-rotate-left",
					_("Rotate-Right"):"object-rotate-right",
					_("Rotate-Twice"):"object-flip-vertical",
					_("Image"):"insert-image",
					_("Import-Pdf"):"application-pdf",
					_("Import-Folder"):"folder-pictures",
					_("Import-Image"):"image",
					_("Invert-List"):"gtk-sort-descending",
					_("Recognize"):"gtk-convert",
					_("Recognize-Selected-Images"):"gtk-convert",
					_("Recognize-All-Images"):"gtk-convert",
					_("Recognize-Selected-with-rotation"):"gtk-convert",
					_("Recognize-All-with-rotation"):"gtk-convert",
					_("Recognize-Selected-Areas"):"gtk-convert",
					_("Clear"):"gtk-clear",
					_("Print"):"gtk-print",
					_("Export-As-Pdf"):"application-pdf",
					_("Print-Preview"):"gtk-print-preview",
					_("Quit"):"gtk-quit",
					_("Edit"):"edit-cut",
					_("Cut"):"gtk-cut",
					_("Copy"):"gtk-copy",
					_("Paste"):"gtk-paste",
					_("Scan"):"scanner",
					_("Scan-Image"):"scanner",
					_("Scan-Image-Repeatedly"):"scanner",
					_("Scan-and-Ocr"):"scanner",
					_("Scan-and-Ocr-Repeatedly"):"scanner",
					_("Optimise-Scanner-Brightness"):"scanner",
					_("Scan-Using-Webcam"):"camera-web",
					_("Take-Screenshort"):"camera-photo",
					_("Take-and-Recognize-Screenshort"):"camera-photo",
					_("Preferences"):"gtk-preferences",
					_("Preferences-Scanning"):"gtk-preferences",
					_("Preferences-General"):"gtk-preferences",
					_("Preferences-Recognition"):"gtk-preferences",
					_("Restore"):"gtk-clear",
					_("Load"):"gtk-open",
					_("Tools"):"accessories-text-editor",
					_("Dictionary"):"accessories-dictionary",
					_("Audio-Converter"):"audio-input-microphone",
					_("Help"):"gtk-help",
					_("Open-Readme"):"gtk-help",
					_("Video-Tutorials"):"gtk-help",
					_("Open-Home-Page"):"gtk-help",
					_("Get-Source-Code"):"gtk-help",
					_("About"):"gtk-about"}
					
