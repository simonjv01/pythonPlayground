
def count_letters(sentence, letter):

    setence_lower = sentence.lower();
    return setence_lower.count(letter.lower());

sentence = "If Fred is from a part of France, then of course Fred's French is good."
letter_to_count = "F";
result = count_letters(sentence,letter_to_count);
print(result);
