# -*- coding: utf-8 -*-
import sys
import classification

def main():
    clf = classification.classification()

    #�f�[�^�t�@�C����ǂݍ���
    clf.load()

#    while True:
#        str = input()
#        print(str)
#        if str == "1":
#            break



##################################################
#��������

#�����o��
#print(clf.queation([0, 1, 2], [1, 3, 5]))

#�񓚂��󂯎��
#input()

#�񓚂����邩�ǂ����𒲂ׂ�
#str = clf.answer([0, 1, 2], [1, 3, 5])
#�����`�Ȃ��(if, else, elsif)

#�񓚂���������o�͂��ă��[�v�𔲂���
#print

#�񓚂��Ȃ�������1�ɖ߂�
#�`�̂�����(while, else)

#�����܂�
##################################################
if __name__ == "__main__":
    sys.exit(int(main() or 0))
