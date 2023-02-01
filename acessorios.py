class Acessorios:
    def __init__(self) -> None:
        self.camera_re = bool()
        self.camera_3d = bool()
        self.farol_led = bool()
        self.farol_milha = bool()
        self.fechamento_mala = bool()
        self.sensor_calibragem_pneus = bool()
        self.ar_condicionado = bool()
        self.painel_digital = bool()
        
    
    def write_camera_re(self, camera_re):
        self.camera_re = camera_re
        
    def write_camera_3d(self, camera_3d):
        self.camera_3d = camera_3d
    
    def write_headlight_led(self, farol_led):
        self.farol_led = farol_led
        
    def write_headlight_milha(self, farol_milha):
        self.farol_milha = farol_milha
        
    def write_close_suitcase(self, fechamento_mala):
        self.fechamento_mala = fechamento_mala
        
    def write_s_calibration_tire(self, sensor_calibragem_pneus):
        self.sensor_calibragem_pneus = sensor_calibragem_pneus
        
    def write_air_conditioner(self, ar_condicionado):
        self.ar_condicionado = ar_condicionado
        
    def write_digital_panel(self, painel_digital):
        self.painel_digital = painel_digital
        
    def read_camera_re(self):
        return self.camera_re
    
    def read_camera_3d(self):
        return self._camera_3d
    
    def read_headlight_led(self):
        return self.farol_led
    
    def read_headlight_milha(self):
        return self.farol_milha
    
    def read_close_suitcase(self):
        return self.fechamento_mala
    
    def read_s_calibration_tire(self):
        return self.sensor_calibragem_pneus
    
    def read_air_conditioner(self):
        return self.ar_condicionado
    
    def read_digital_panel(self):
        return self.painel_digital