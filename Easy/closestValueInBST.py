def closestValueInBst(tree, target):
    return closestValueInBstHelper(tree, target, float("inf"))

def closestValueInBstHelper(tree, target, closest):
    #since it is a recursive function, we need to write base case
    if tree == None:
        return closest:
    if (target - closest) > (target - tree.value):
        closest = tree.value
    if target > tree.value:
        return closestValueInBstHelper(tree.right, target, closest)
    elif target < tree.value:
        return closestValueInBstHelper(tree.left, target, closest)
