
def main_func1():
    """
    На вход строка 2{as3{qwe}} → asqweqweqweasqweqweqwe
    Т.е у тебя метаязык, число_повторений{что_повторяем}, некоторой степени вложенности
    :return:
    """
    proc_str(in_str='2{as3{qwe}}', do_print=True)
    proc_str_vai_eval(in_str='2{as3{qwe}}', do_print=True)
    assert proc_str(in_str='2{as3{qwe}}') == 'asqweqweqweasqweqweqwe'
    assert proc_str_vai_eval(in_str='2{as3{qwe}}') == 'asqweqweqweasqweqweqwe'


def proc_str(in_str: str = '', do_print: bool = False) -> str:
    if do_print:
        print(f'{in_str}', end=' -> ')
    sublines = in_str.split('{')
    current_line = 0
    _line_tot = ''
    for _i in reversed(range(len(sublines))):
        _line_step = ''
        current_line = current_line + 1
        if current_line == 1:
            _line_tot = str(sublines[_i].replace('}',''))
        else:
            do_times = int(sublines[_i][-1])
            _line_step = sublines[_i].replace(str(do_times),'')
            _line_tot = _line_step + out_str(do_times=do_times,in_str=_line_tot)
    if do_print:
        print(f'{_line_tot}')
    return _line_tot


def out_str(do_times: int, in_str: str) -> str:
    str_out = in_str * do_times
    # for _i in range(do_times):
    #     str_out = str_out + in_str
    return str_out


def proc_str_vai_eval(in_str: str = '', do_print: bool = False) -> str:
    if do_print:
        print(f'{in_str}', end=' -> ')
    line_in = in_str
    not_first_digit = False
    prev_closed_bracket = False
    expression_for_eval = ''
    for _each_letter in line_in:
        step_repl = ''
        if _each_letter.isnumeric():
            if not_first_digit:
                step_repl = '" + ' + str(_each_letter) + '*'
            else:
                step_repl = str(_each_letter) + '*'
                not_first_digit = True
        elif _each_letter == '{':
            step_repl = '("'
        elif _each_letter == '}':
            if prev_closed_bracket:
                step_repl = ')'
            else:
                step_repl = '")'
            prev_closed_bracket = True
        else:
            step_repl = _each_letter
            if _each_letter != '}':
                prev_closed_bracket = False
        expression_for_eval = expression_for_eval + step_repl
    line_out = eval(expression_for_eval)
    if do_print:
        print(f'{line_out}')
    return line_out


if __name__ == '__main__':
    main_func1()

