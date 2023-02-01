class Seguranca:
    def __init__(self) -> None:
        self.vidros_reforcados = bool()
        self.cintos_3_pontas = bool()
        self.airbag = bool()
        self.controle_estabilidade = bool()
        self.sensor_fadiga = bool()
        self.sensor_frenagem = bool()
        self.sensor_p_cego = bool()
    
    def write_glass_reforced(self, vidros_reforcados: bool) -> None:
        self.vidros_reforcados = vidros_reforcados
        
    def write_3_point_belt(self, cintos_3_pontas: bool) -> None:
        self.cintos_3_pontas = cintos_3_pontas
        
    def write_airbag(self, airbag: bool) -> None:
        self.airbag = airbag
        
    def write_stability_control(self, controle_estabilidade: bool) -> None:
        self.controle_estabilidade = controle_estabilidade
        
    def write_s_fadigue(self, sensor_fadiga: bool) -> None:
        self.sensor_fadiga = sensor_fadiga
        
    def write_s_braking(self, sensor_frenagem: bool) -> None:
        self.sensor_frenagem = sensor_frenagem
        
    def write_s_blind_spot(self, sensor_p_cego: bool) -> None:
        self.sensor_p_cego = sensor_p_cego
        
    def read_glass_reforced(self) -> str:
        return str(self.vidros_reforcados)
    
    def read_3_point_belt(self) -> str:
        return str(self.cintos_3_pontas)
    
    def read_airbag(self) -> str:
        return str(self.airbag)
    
    def read_stability_control(self) -> str:
        return str(self.controle_estabilidade)
    
    def read_s_fadigue(self) -> str:
        return str(self.sensor_fadiga)
    
    def read_s_braking(self) -> str:
        return str(self.sensor_frenagem)
    
    def read_s_blind_spot(self) -> str:
        return str(self.sensor_p_cego)
    
    def read_all_security(self) -> dict:
        dicio = {'Vidros Reforcados': self.vidros_reforcados, 'Cintos 3 Pontas': self.cintos_3_pontas, 'airbag': self.airbag, 'Controle Estabilidade': self.controle_estabilidade,
                 'Sensor Fadiga': self.sensor_fadiga, 'Sensor Frenagem': self.sensor_frenagem, 'Sensor de Ponto Cego': self.sensor_p_cego}
        return dicio