from p6_game import Simulator

analysis = {'prev': {}, 'coords': {}}


def analyze(design):
    global analysis
    sim = Simulator(design)
    analysis = {}
    init = sim.get_initial_state()
    analysis['prev'] = {}
    analysis['prev'][init] = None
    analysis['coords'] = {}
    Q = [init]

    while Q:
        node = Q.pop(0)
        for move in sim.get_moves():
            next = sim.get_next_state(node, move)
            if next is not None and next not in analysis['prev']:
                Q.append(next)
                analysis['prev'][next] = node
                if next[0] not in analysis['coords']:
                    analysis['coords'][next[0]] = []
                analysis['coords'][next[0]].append(next)
    # TODO: fill in this function, populating the ANALYSIS dict


def inspect((i,j), draw_line):
    init = (i, j)
    states = analysis['coords'][init]
    color = 1
    for state in states:
        while analysis['prev'][state]:
            prev = analysis['prev'][state]
            draw_line(prev[0], state[0],color+1,color)
            state = prev
        color += 1
    # TODO: use ANALYSIS and (i,j) draw some lines
