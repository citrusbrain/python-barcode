import barcode
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:', sys.argv[0], '<barcode> <text>', file=sys.stderr)
        exit(-1)
    code = sys.argv[1]
    text = sys.argv[2]

    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(sys.argv[1])
    ean.writer.strokes = [0.] + [.5 for _ in text.split('\n')]
    ean.save('ean13_barcode', text=code + '\n' + text)
