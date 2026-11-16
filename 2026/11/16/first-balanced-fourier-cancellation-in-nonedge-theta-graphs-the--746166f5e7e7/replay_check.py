"""Replay both independent exact integer constructions and compare every coefficient."""
from itertools import combinations_with_replacement
from direct_check import census,run as direct_run
from transfer_check import spectrum,run as transfer_run
import json

def run():
    a=direct_run();b=transfer_run()
    assert a==b
    checked=0
    for lengths in combinations_with_replacement(range(2,8),3):
        if sum(lengths)>9:continue
        first=census(lengths)['spectrum']
        second=spectrum(lengths)
        assert first==second,lengths
        checked+=len(first)
    assert checked==243+729+2187+6561+2187+6561+6561
    return {'full_frequency_vectors_compared':checked,
            'table':a,'status':'PASS'}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,separators=(',',':')))
