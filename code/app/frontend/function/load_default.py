def UseDefaultValue(theme, bg_col, main_col, second_col, img):

	if theme == None:
		theme = "gnome_dark"

	if bg_col == None and 'dark' in theme:
		bg_col = "black"
	elif bg_col == None and 'light' in theme:
		bg_col = "white"

	if main_col == None:
		main_col = "lightgreen"

	if second_col == None and bg_col == "black":
		second_col = "white"
	elif second_col == None and bg_col == "white":
		second_col = "black"

	if second_col == None:
		second_col = "white"

	if img == None:
		img = "octocat"

	return theme, bg_col, main_col, second_col, img