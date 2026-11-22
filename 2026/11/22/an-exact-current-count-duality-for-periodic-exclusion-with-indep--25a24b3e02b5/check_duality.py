"""Exact finite-state checks for particle-hole/obstacle reflection on periodic rings.

The arbitrary-ring theorem is proved algebraically in RESULT.md; this checker is
finite diagnostic evidence, not a proof for untested ring lengths.
"""
from fractions import Fraction
from itertools import product


def dual(eta, obs, delta):
    n = len(eta)
    return (tuple(1 - eta[(-j) % n] for j in range(n)),
            tuple(obs[(2 * delta - 1 - j) % n] for j in range(n)))


def events(eta, obs, delta, base, slow, bind, unbind):
    n = len(eta)
    for i in range(n):
        if eta[i] == 1 and eta[(i + 1) % n] == 0:
            r = slow if obs[(i + delta) % n] else base
            if r:
                newer = list(eta)
                newer[i] = 0
                newer[(i + 1) % n] = 1
                yield ('hop', i, tuple(newer), obs, r)
        later = list(obs)
        later[i] = 1 - later[i]
        r = unbind if obs[i] else bind
        yield ('obstacle', i, eta, tuple(later), r)


def check():
    tested_states = 0
    tested_events = 0
    tested_involutions = 0
    rates = [
        (Fraction(7, 3), Fraction(0), Fraction(2, 7), Fraction(9, 5)),
        (Fraction(9, 4), Fraction(1, 3), Fraction(8, 9), Fraction(3, 2)),
        (Fraction(13, 5), Fraction(13, 5), Fraction(7, 8), Fraction(4, 11)),
    ]
    for n in range(2, 8):
        bits = list(product((0, 1), repeat=n))
        for eta in bits:
            for obs in bits:
                for delta in (0, 1):
                    mapped = dual(eta, obs, delta)
                    assert dual(*mapped, delta) == (eta, obs)
                    assert sum(mapped[0]) == n - sum(eta)
                    tested_involutions += 2
                    for base, slow, bind, unbind in rates:
                        original = list(events(eta, obs, delta, base, slow, bind, unbind))
                        transformed = list(events(*mapped, delta, base, slow, bind, unbind))
                        images = {}
                        for kind, site, nxt_eta, nxt_obs, rate in transformed:
                            key = kind, site, nxt_eta, nxt_obs
                            assert key not in images
                            images[key] = rate
                        assert len(original) == len(images)
                        tested_states += 1
                        for kind, site, nxt_eta, nxt_obs, rate in original:
                            image_eta, image_obs = dual(nxt_eta, nxt_obs, delta)
                            if kind == 'hop':
                                newsite = (-site-1) % n
                            else:
                                newsite = (2 * delta-1-site) % n
                            key = kind, newsite, image_eta, image_obs
                            assert images[key] == rate, (n, eta, obs, delta, key)
                            tested_events += 1
    print(f"PASS; rings n=2,...,7; {tested_involutions} involution/sector checks; "
          f"{tested_states} generator transition rows; {tested_events} labelled event comparisons; "
          "3 exact-rational rate regimes, 2 gate placements.")

if __name__ == '__main__':
    check()
