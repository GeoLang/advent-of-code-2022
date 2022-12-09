# f = open("sample_input.txt", "r")
f = open("input.txt", "r")
stream = f.readline().strip()
f.close()

first_chunk_idx = 0
for idx, char in enumerate(stream):
    if idx <= len(stream) - 4:
        chunk = stream[idx:idx+4]
        if len(set(chunk)) == 4:
            first_chunk_idx = idx + 4
            break

print(f"Part A: {first_chunk_idx}")

first_message_idx = 0
for idx, char in enumerate(stream):
    if idx <= len(stream) - 14:
        chunk = stream[idx:idx+14]
        if len(set(chunk)) == 14:
            first_message_idx = idx + 14
            break

print(f"Part B: {first_message_idx}")
