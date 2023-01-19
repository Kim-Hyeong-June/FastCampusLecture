class Unit:
    """
    속성 : 이름 , 체력 , 방어막 , 공격력
    """
    count = 0

    # 생성자 (constructor)
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name , hp , shield , demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1

        print(f"[{self.name}](이)가 생성 되었습니다.")

    def hit(self,demage):
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield = 0

        if demage > 0:
            if self.hp > demage:
                self.hp -= demage
            else:
                self.hp = 0

    def __str__(self):
        return f"[{self.name}] 체력  : {self.hp} 방어막 : {self.shield} 공격력 : {self.demage}"
    
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 수 : [{cls.count}] 개")


probe = Unit("프로브" , 20 , 20 , 5)
zealot = Unit("질럿" , 100 , 60 , 16)
dragon = Unit("드라군" , 100 , 80 , 20)

Unit.print_count()
probe.hit(15)
print(probe.demage)

print(dir(probe))
