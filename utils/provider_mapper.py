def map_provider(raw):
    raw = raw.upper()

    if "PRAGMATIC" in raw:
        return "PRAGMATIC"
    if "PSG" in raw:
        return "PSG PRIMESIGMA"
    if "PGS" in raw:
        return "PGS PEGASUS"
    if "PG" in raw:
        return "PG"
    if "JILI" in raw:
        return "JILI"
    if "NAGA" in raw:
        return "NAGAGAME"
    if "JOKER" in raw:
        return "JOKER"
    if "YGG" in raw:
        return "YGG"
    if "SPADE" in raw:
        return "SPADE"
    if "RELAX" in raw:
        return "RELAX"
    if "EVOPLAY" in raw:
        return "EVOPLAY"
    if "BLUEPRINT" in raw:
        return "BLUEPRINT"
    if "NEXTSPIN" in raw:
        return "NEXTSPIN"
    if "ADVANT" in raw:
        return "ADVANTPLAY"
    if "MIMI" in raw:
        return "MIMI"

    return raw