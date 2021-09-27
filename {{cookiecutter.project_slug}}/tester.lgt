% Tester for {{ cookiecutter.project_name }}

:- initialization((
	set_logtalk_flag(report, warnings),
	logtalk_load([ % Dependencies
	]),
	logtalk_load(lgtunit(loader)),
	logtalk_load([
		{{ cookiecutter.project_slug }}
	], [
		source_data(on),
		debug(on)
	]),
	logtalk_load(tests, [hook(lgtunit)]),
	tests::run
)).
