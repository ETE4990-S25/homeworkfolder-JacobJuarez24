def decode(message_file):
    #Read file and store the number-word pair
    with open(message_file, 'r') as file:
        #Read lines, split them between number and word, store them as tuple
        num_word_list = []
        for line in file:
            number, word = line.split()
            num_word_list.append((int(number), word))

    #Sort list by number
    num_word_list.sort(key=lambda x: x[0])

    #Start from number 1
    decoded_message = []
    current_num = 1

    #Start creating pyramid
    while current_num <= len(num_word_list):
        row_length = current_num
        row_end = current_num + row_length - 1

        #Match the word to the last number in the row
        if row_end <= len(num_word_list):
            for num, word in num_word_list:
               if num == row_end:
                    decoded_message.append(word)
                    break

        #Move to next row
        currenr_num = row_end + 1

    #Join the words to form decoded message
    return ' '.join(decoded_message)