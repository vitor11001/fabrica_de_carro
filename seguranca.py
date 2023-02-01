class Seguranca:
    def __init__(self) -> None:
        self.vidros_reforcados = bool()
        self.cintos_3_pontas = bool()
        self.airbag = bool()
        self.controle_estabilidade = bool()
        self.sensor_fadiga = bool()
        self.sensor_frenagem = bool()
        self.sensor_p_cego = bool()
    
    def write_glass_reforced(self, vidros_reforcados):
        self.vidros_reforcados = vidros_reforcados
        
    def write_3_point_belt(self, cintos_3_pontas):
        self.cintos_3_pontas = cintos_3_pontas
        
    def write_airbag(self, airbag):
        self.airbag = airbag
        
    def write_stability_control(self, controle_estabilidade):
        self.controle_estabilidade = controle_estabilidade
        
    def write_s_fadigue(self, sensor_fadiga):
        self.sensor_fadiga = sensor_fadiga
        
    def write_s_braking(self, sensor_fadiga):
        self.sensor_frenagem = sensor_frenagem
        
    def write_s_blind_spot(self, sensor_p_cego):
        self.sensor_p_cego = sensor_p_cego