import mido

NOTENAME = [
    "C-1",
    "CS-1",
    "D-1",
    "DS-1",
    "E-1",
    "F-1",
    "FS-1",
    "G-1",
    "GS-1",
    "A-1",
    "AS-1",
    "B-1",
    "C0",
    "CS0",
    "D0",
    "DS0",
    "E0",
    "F0",
    "FS0",
    "G0",
    "GS0",
    "A0",
    "AS0",
    "B0",
    "C1",
    "CS1",
    "D1",
    "DS1",
    "E1",
    "F1",
    "FS1",
    "G1",
    "GS1",
    "A1",
    "AS1",
    "B1",
    "C2",
    "CS2",
    "D2",
    "DS2",
    "E2",
    "F2",
    "FS2",
    "G2",
    "GS2",
    "A2",
    "AS2",
    "B2",
    "C3",
    "CS3",
    "D3",
    "DS3",
    "E3",
    "F3",
    "FS3",
    "G3",
    "GS3",
    "A3",
    "AS3",
    "B3",
    "C4",
    "CS4",
    "D4",
    "DS4",
    "E4",
    "F4",
    "FS4",
    "G4",
    "GS4",
    "A4",
    "AS4",
    "B4",
    "C5",
    "CS5",
    "D5",
    "DS5",
    "E5",
    "F5",
    "FS5",
    "G5",
    "GS5",
    "A5",
    "AS5",
    "B5",
    "C6",
    "CS6",
    "D6",
    "DS6",
    "E6",
    "F6",
    "FS6",
    "G6",
    "GS6",
    "A6",
    "AS6",
    "B6",
    "C7",
    "CS7",
    "D7",
    "DS7",
    "E7",
    "F7",
    "FS7",
    "G7",
    "GS7",
    "A7",
    "AS7",
    "B7",
    "C8",
    "CS8",
    "D8",
    "DS8",
    "E8",
    "F8",
    "FS8",
    "G8",
    "GS8",
    "A8",
    "AS8",
    "B8",
    "C9",
    "CS9",
    "D9",
    "DS9",
    "E9",
    "F9",
    "FS9",
    "G9",
]
PINNAME = "buzzer_pin"
tempo = 500
ticks_per_beat = 480


def ticks2ms(ticks: int):
    global tempo, ticks_per_beat
    return round(ticks * tempo / ticks_per_beat)


def main():
    global tempo
    print("midiファイルの名前", end="：")
    midfile_name = input()
    midfile = mido.MidiFile(midfile_name)
    txtfile_name = midfile_name.rstrip(".mid") + ".txt"
    txtfile = open(txtfile_name, "w")

    i = 0
    print("トラック一覧")
    for t in midfile.tracks:
        print(f"[{i}]:{t}")
        i += 1
    print("どのトラックにしますか", end="：")
    tracknum = int(input())

    ticks_per_beat = midfile.ticks_per_beat
    print(f"ticks_per_beat = {ticks_per_beat}")

    for message in midfile.tracks[0]:
        if message.type == "set_tempo":
            tempo = message.tempo / 1000
            bpm = round(mido.tempo2bpm(message.tempo))
            print(f"bpm = {bpm}")

    for message in midfile.tracks[tracknum]:
        if message.type == "note_off":
            milis = ticks2ms(message.time)
            txtfile.write(f"tone({PINNAME},NOTE_{NOTENAME[message.note]},{milis});\n")
            txtfile.write(f"delay({milis});\n")

        if message.type == "note_on" and message.time > 0:
            milis = ticks2ms(message.time)
            txtfile.write(f"delay({milis});\n")

    bar = midfile.ticks_per_beat * 4
    bar_milis = ticks2ms(bar)
    txtfile.write(f"delay({bar_milis});\n")

    print("完了しました")
    print(f"出力先：{txtfile_name}")


if __name__ == "__main__":
    main()
