
def find_word(text_):
    global cmd
    text = []
    #text = text.split(' ')  # Untuk sortir per kata
    text.append(text_)       # Untuk sortir semua kalimat sekaligus
    for i in range(0, len(text)):
        if text[i] in right_possibility:
            print('kanan')
            cmd = 'kanan\r'
        elif text[i] in left_possibility:
            print('kiri')
            cmd = 'kiri\r'
        elif text[i] in upper_possibility:
            print('atas')
            cmd = 'atas\r'
        elif text[i] in lower_possibility:
            print('bawah')
            cmd = 'bawah\r'
        elif text[i] in forward_possibility:
            print('maju')
            cmd = 'maju\r'
        elif text[i] in backward_possibility:
            print('mundur')
            cmd = 'mundur\r'
        elif text[i] in open_possibility:
            print('buka')
            cmd = 'buka\r'
        elif text[i] in close_possibility:
            print('tutup')
            cmd = 'tutup\r'            
        else:
            cmd = 'junk'
            pass
    return cmd

right_possibility = ['canon','gardner' ,'gannon', 'hannan', 'annan', 'cannon', 'adnan']
left_possibility = ['geary','hearing' ,'cookie', 'kidney', 'guilty', 'deputy', 'duty', 'getty', 'kitty', 'katie', 'geely', 'giddy']
upper_possibility = ['at last', 'this', 'thus', 'us', 'pass', 'last', 'atlast', 'at atlast', 'i pass', 'pass', 'what does', 'at us', 'how does', 'a pass', 'at this', 'at thus','bus',  'at bus' ]
lower_possibility = ['cooper','boa', 'her', 'bella' ,'power', 'wow','coppola', 'whoa', 'woah']
forward_possibility = ['my too', 'to', 'much too', 'my to','mine too', 'too', 'much']
backward_possibility = ['more', 'do','more dude', 'dude','more do', 'my daughter', 'wonder', 'daughter','one do', 'one']
open_possibility = ['hooker', 'booker', 'poker', 'book']
close_possibility = ['to to', 'though to', 'though the', 'the top', 'to top','top', 'though']

# Test the List
'''
while True:
    text = str(input('here: '))
    find_word(right_possibility, left_possibility, upper_possibility, lower_possibility, text)
'''        