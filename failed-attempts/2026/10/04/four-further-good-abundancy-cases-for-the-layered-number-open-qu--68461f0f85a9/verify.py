#!/usr/bin/env python3
# Exact arithmetic replay for the four witness cases.

cases = {
    14: {"q":83, "q_first":37, "q_next":572, "target_first":425, "mult_num":710, "mult_den":1},
    15: {"q":149, "q_first":52, "q_next":1500, "target_first":673, "mult_num":2, "mult_den":21},
    16: {"q":127, "q_first":47, "q_next":1145, "target_first":1072, "mult_num":1, "mult_den":2},
    17: {"q":13633, "q_first":1687, "q_next":None, "target_first":1727, "mult_num":1630, "mult_den":1},
}

for i, d in cases.items():
    q = d["q"]
    assert d["q_first"] <= d["target_first"]
    if d["q_next"] is not None:
        assert d["target_first"] < d["q_next"]
    assert d["mult_num"] % q != 0
    assert d["mult_den"] % q != 0
    assert (q + 1) % i == 0

# For i=17 the published b-file segment from 1687 through 1727
# contains 13633 only at its first position; the segment is encoded
# explicitly to make the finite check independent of text parsing.
segment_17 = [
13633,13649,13669,13679,13681,13687,13691,13693,13697,13709,13711,
13721,13723,13729,13751,13757,13759,13763,13781,13789,13799,13807,
13829,13831,13841,13859,13873,13877,13879,13883,13901,13903,13907,
13913,13921,13931,13933,13963,13967,13997,13999
]
assert len(segment_17) == 41
assert segment_17.count(13633) == 1
assert segment_17[-1] == 13999

print("VERIFY_OK")
