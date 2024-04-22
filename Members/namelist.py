def read(group: str):
    with open(f"{group}.txt", "r") as f:
        names = f.readlines()

    for i, name in enumerate(names):
        if name.startswith("#") or name.startswith("!"):
            names[i] = None
        else:
            names[i] = name.strip()

    return [n.lower() for n in names if bool(n)]

def checkperm(username: str, groupName: str):
    group = read(groupName)
    
    if username.lower() in group:
        return True
    else:
        return False

def parseHead(head: str):
    headers = head.split("\n")
    header = {}
    for h in headers:
        h = h.strip()
        if not h.startswith("!"):
            continue

        h = h[1:]
        hname, hval = h.split(":", 1)
        hname = hname.strip()
        hval = hval.strip().split()
        header[hname] = header.get(hname, []) + [hval]
    


if __name__=='__main__':
    print(read('Council'))
    print(checkperm('@BernieHuang2008', 'CoreMembers'))
    print(checkperm('@Nathancgy', 'Council'))
    print(parseHead("""
                    # This is Comment
                    ! allow-modify: Council<VoteRate:0.2>
                    ! allow-modify: CoreMembers<VoteRate:0.34>
                    """))
    print(parseHead("!allow-modify: Council<VoteRate:1.0>"))
