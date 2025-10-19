
def predictTheWinner(nums: list[int]) -> bool:

    # Puntuacion de p1 (se resta la puntuacion de p2)
    score = 0

    # True = p1, False = p2
    turno = True

    for i in enumerate(nums):

        # Si el penultimo y el segundo son iguales, o si el primero es menor que el segundo
        # y el ultimo es menor que el penultimo
        if nums[1] == nums[-2] or nums[0] < nums[1] and nums[-1] < nums[-2]:

            # Si el primero es mayor que el ultimo
            if nums[0] > nums[-1]:
                
                if turno:
                    score += nums.pop(0)
                else:
                    score -= nums.pop(0)
            else:
                if turno:
                    score += nums.pop(-1)
                else:
                    score -= nums.pop(-1)

            turno = not turno

            continue

        # Si el primero es mayor o igual al segundo
        if nums[0] >= nums[1]:
            if turno:
                score += nums.pop(0)
            else:
                score -= nums.pop(0)
        elif nums[-1] >= nums[-2]:
            if turno:
                score += nums.pop(-1)
            else:
                score -= nums.pop(-1)

        turno = not turno

    # Devolver True solo si score es menor a 0
    if score < 0:
        return False
    
    return True