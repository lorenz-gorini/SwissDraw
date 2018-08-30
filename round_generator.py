
def allTaken(taken):
    for i in taken:
        if not i:
            return False
    return True

# Function that calls the recursive procedure and sets things up
# If ignoreTop is specified, ignore the top ignoreTop teams when chosing the new matchups
# ignoreTop should be even
def generatePairs(leaderboard, A, ignoreTop = 0):
    taken = [False] * len(leaderboard)
    # Make sure the first few are ignroed. Have them already be taken
    for i in range(ignoreTop):
        taken[i] = True
    
    pairs = []
    generatePairsRec(leaderboard, A, 0, taken, pairs)
    return pairs

# Generate new matchups with A and leaderboad
# Returns true if successful. The pairs list provided is filled with pairs of indexes.
def generatePairsRec(leaderboard, A, currentI, taken, pairs):    
    if(allTaken(taken)):
        return True

    if(taken[currentI]):
        return generatePairsRec(leaderboard, A, currentI + 1, taken, pairs)

    # Look for another team
    for otherI in range(currentI + 1, len(leaderboard)):
        other = leaderboard[otherI]
        current = leaderboard[currentI]

        # Check if other is available
        if(taken[otherI]):
            continue

        # Check if matched before
        haveMatchedBefore = False
        for match in A:
            if(match[current] != 0 and match[other] != 0):
                haveMatchedBefore = True
        if(haveMatchedBefore):
            continue

        # If all other things passed, add the pair
        pairs.append((currentI, otherI))
        taken[currentI] = True
        taken[otherI] = True

        # Do recursion and check if it worked
        result = generatePairsRec(leaderboard, A, currentI+1, taken, pairs)
        if(result):
            return True
        else:
            # Undo last and continue
            pairs.pop(len(pairs) - 1)
            taken[currentI] = False
            taken[otherI] = False
            continue
