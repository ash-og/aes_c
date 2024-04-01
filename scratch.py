import ctypes
from aes.aes import bytes2matrix as p_bytes2matrix, matrix2bytes, sub_bytes as p_sub_bytes # importing python subbytes

rijndael = ctypes.CDLL('./rijndael.so')

buffer = b'\x00\x01\x02\x03\x04\x05\x06\x07'
buffer += b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
block = ctypes.create_string_buffer(buffer)

CMatrixType = (ctypes.c_ubyte * 4) * 4  # Defines a 4x4 matrix of unsigned bytes
c_matrix = CMatrixType()

p_matrix = p_bytes2matrix(buffer)
rijndael.bytes2matrix(block, c_matrix)

# Call the C sub_bytes function
rijndael.sub_bytes(c_matrix)
p_sub_bytes(p_matrix)

print("C results: ", ctypes.string_at(c_matrix,16))
print("Python results: ", matrix2bytes(p_matrix))

print(ctypes.string_at(c_matrix,16)==matrix2bytes(p_matrix))
