# Add the functions in this file
import json
def load_journal(fname):
    f = open(fname)
    d = f.read()
    s = json.loads(d)
    return s

def compute_phi(fname, event):
    d = load_journal(fname)
    n11 = n10 = n01 = n00 = 0
    for day in d:
        if event in day['events']:
            if day['squirrel'] == True:
                n11 += 1
            else:
                n10 += 1
        else:
            if day['squirrel'] == True:
                n01 += 1
            else:
                n00 += 1

    n1_ = n11 + n10
    n0_ = n01 + n00
    n_1 = n01 + n11
    n_0 = n10 + n00

    corr = (n11 * n00 - n10 * n01) / (n1_ * n0_ * n_1 * n_0)**0.5
    return corr

def compute_correlations(fname):
    d = load_journal(fname)
    event = []
    for day in d:
        for i in day['events']:
            if i not in event:
                event.append(i)
    correlations = {}
    for i in event:
        correlations[i] = compute_phi(fname, i)
    return correlations

def diagnose(fname):
    d = compute_correlations(fname)
    high = -1
    low = 1
    for event in d:
        if d[event] > high:
            high = d[event]
            high_event = event
        if d[event] < low:
            low = d[event]
            low_event = event

    return [high_event, low_event]
