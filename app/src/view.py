
def create_canvas():
    canva_h = 32
    canva_w = 16

    canvas = [[' ' for i in range(0, canva_w)] for j in range(0, canva_h)]

    
    return canvas, canva_w


def show_to_console(branch):
    print(branch)
    canvas, canva_w = create_canvas()
    canvas = branch_on_vancas(canvas, branch, canva_w)


def branch_on_vancas(canvas, branch, canva_w, space=32):
    for x in branch:
        print(return_int(x))
    


def return_int(point):

    if isinstance(point, int):
        return point
    elif isinstance(point, list):
        for x in point:
            return_int(x)
