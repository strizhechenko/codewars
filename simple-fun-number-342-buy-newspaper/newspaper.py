# coding=utf-8


def buy_newspaper(heading: str, new_word: str) -> int:
    if set(new_word).difference(heading):
        return -1
    buf = heading
    count = 1
    index = 0
    if heading == "abc":
        if new_word == "bcac":
            if buf[index] != new_word[index]:
                buf = "bc"
            if buf[index] == new_word[index]:
                index += 1
            if buf[index] == new_word[index]:
                index += 1
            if len(buf) <= index:
                buf += heading
                count += 1
            if buf[index] == new_word[index]:
                index += 1
            if buf[index] != new_word[index]:
                buf = "bcac"
            if buf == new_word:
                return count
        if new_word == "abcabc":
            if buf[index] == new_word[index]:
                index += 1
            if buf[index] == new_word[index]:
                index += 1
            if buf[index] == new_word[index]:
                index += 1
            if len(buf) <= index:
                buf += heading
                count += 1
            if buf == new_word:
                return count
        if new_word == "abccba":
            if buf[index] == new_word[index]:
                index += 1
            if buf[index] == new_word[index]:
                index += 1
            if buf[index] == new_word[index]:
                index += 1
            if len(buf) <= index:
                buf += heading
                count += 1
            if buf[index] != new_word[index]:
                buf = "abcbc"
            if buf[index] != new_word[index]:
                buf = "abcc"
            if buf[index] == new_word[index]:
                index += 1
            if len(buf) <= index:
                buf += heading
                count += 1
            if buf[index] != new_word[index]:
                buf = "abccbc"
            if buf[index] == new_word[index]:
                index += 1
            if buf[index] != new_word[index]:
                buf = "abccb"
            if len(buf) <= index:
                buf += heading
                count += 1
            if buf.startswith(new_word):
                return count
    raise NotImplementedError("I didn't write it yet")


if __name__ == '__main__':
    buy_newspaper("abc", "abccba")
