dinner_invitation = ['akeodi', 'kiikpoye', 'kubi', 'imabin']
message = f"Hello {dinner_invitation[2].title()}, I would like to invite you to dinner at my place."
print(message)
cannot_make = dinner_invitation.pop(2)
print(f'{cannot_make.title()} cannot make it to dinner')
print(dinner_invitation)
dinner_invitation.insert(2, 'akari')
print(dinner_invitation)
print(f"Hello {dinner_invitation[2].title()}, I would like to invite you to dinner at my place.")

print(f'Hello {dinner_invitation[0]}, {dinner_invitation[1]}, {dinner_invitation[2]}, and {dinner_invitation[3]}, I have found a bigger dinner table.')
dinner_invitation.insert(0, 'paul')
print(dinner_invitation)
dinner_invitation.insert(2, 'justina')
dinner_invitation.append('bright')
print(f'Hello {dinner_invitation[0]}, {dinner_invitation[1]}, {dinner_invitation[2]}, {dinner_invitation[3]}, {dinner_invitation[4]}, and {dinner_invitation[5]}, Can you join me for dinner.')
print('I can only invite two people for dinner')
A = dinner_invitation.pop()
print(f'Sorry {A.title()} I cannot invite you for dinner')
B = dinner_invitation.pop()
print(f'Sorry {B.title()} I cannot invite you for dinner')
C = dinner_invitation.pop()
print(f'Sorry {C.title()} I cannot invite you for dinner')
D = dinner_invitation.pop()
print(f'Sorry {D.title()} I cannot invite you for dinner')
print(dinner_invitation)
print(f'Hello {dinner_invitation[0]}, {dinner_invitation[2]} and {dinner_invitation[1]}, you are still invited for dinner')
del dinner_invitation[1]
del dinner_invitation[0]
del dinner_invitation[0]
print(dinner_invitation)