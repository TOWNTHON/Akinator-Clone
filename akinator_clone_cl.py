# -*- coding: utf-8 -*-
import sys
import classification

def main():
    clf = classification.classification()

    #�f�[�^�t�@�C����ǂݍ���
    clf.load()

##################################################
#��������

    #��������������l�̖��O�A����Ȃ�������󕶎�
    print(clf.answer([0, 1, 2], [1, 3, 5]))

     #��肪�Ԃ��Ă���
    print(clf.queation([0, 1, 2], [1, 3, 5]))

#�����܂�
##################################################
if __name__ == "__main__":
    sys.exit(int(main() or 0))
