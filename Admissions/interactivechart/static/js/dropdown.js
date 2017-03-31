function getEthnicity() {
	var e = document.getElementById("ethnicity");
	return e.options[e.selectedIndex].text;
}

function getGender() {
	var e = document.getElementById("gender");
	return e.options[e.selectedIndex].text;
}

function getResidency() {
	var e = document.getElementById("residency");
	return e.options[e.selectedIndex].text;
}

function getCollege() {
	var e = document.getElementById("college");
	return e.options[e.selectedIndex].text;
}
