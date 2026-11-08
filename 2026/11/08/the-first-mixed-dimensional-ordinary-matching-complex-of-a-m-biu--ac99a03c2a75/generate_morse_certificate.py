#!/usr/bin/env python3
"""Construct a textual integer discrete-Morse certificate for M_16.

The required verifier regenerates and checks every certificate field.
"""
import json
from pathlib import Path
from verify_m16 import graph_edges, face_complex, verified_acyclic_matching, morse_differentials

edges = graph_edges()
faces = face_complex(edges)
pairs, critical, incidence_count = verified_acyclic_matching(faces, len(edges))
_, differential = morse_differentials(critical, pairs)
certificate = {
    'graph': 'M16',
    'edges': [list(e) for e in edges],
    'matching_pairs': [list(p) for p in pairs],
    'critical_masks': sorted(critical),
    'd4': [[int(v) for v in row] for row in differential[4].tolist()],
    'd5': [[int(v) for v in row] for row in differential[5].tolist()],
    'hasse_incidences': incidence_count,
}
Path(__file__).with_name('morse_certificate.json').write_text(
    json.dumps(certificate, separators=(',', ':'), ensure_ascii=False) + '\n', encoding='utf-8')
print('CERTIFICATE_GENERATED', len(pairs), len(critical))
