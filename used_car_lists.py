makers = ['Chrysler', 'Nissan', 'Hyundai', 'Honda', 'Toyota', 'Chevrolet',
       'Mercedes', 'MINI', 'Lexus', 'Land Rover', 'GMC', 'Mazda', 'Ford',
       'Kia', 'Genesis', 'Cadillac', 'Geely', 'MG', 'Jeep', 'INFINITI',
       'Dodge', 'Ferrari', 'Great Wall', 'Jaguar', 'GAC', 'Renault',
       'Suzuki', 'Peugeot', 'Changan', 'HAVAL', 'BMW', 'Porsche',
       'Mitsubishi', 'Subaru', 'Zhengzhou', 'Lincoln', 'Daihatsu', 'FAW',
       'Chery', 'Isuzu', 'Audi', 'Volkswagen', 'Fiat', 'Mercury',
       'Hummer', 'BYD', 'Maserati', 'Lifan', 'Bentley', 'Foton',
       'Aston Martin', 'Other', 'Victory Auto', 'Škoda', 'Iveco']

types = {'Chrysler': ['C300', '300', 'S300', 'C200', 'SRT'],
 'Nissan': ['Sunny',
  'Patrol',
  'Bus Urvan',
  'Datsun',
  'Maxima',
  'Sylvian Bus',
  'Z370',
  'X-Trail',
  'Land Cruiser Pickup',
  'Altima',
  'Navara',
  'Sentra',
  'Pathfinder',
  'X-Terra',
  'VTC',
  'KICKS',
  'Armada',
  'Juke',
  'Murano',
  'Z350'],
 'Hyundai': ['Elantra',
  'Tucson',
  'Accent',
  'Sonata',
  'Azera',
  'Kona',
  'Senta fe',
  'Genesis',
  'Creta',
  'H1',
  'Veloster',
  'Coupe S',
  'Bus County',
  'Avante',
  'Other',
  'Tuscani',
  'i40',
  'Coupe',
  'Veracruz'],
 'Honda': ['Accord',
  'Civic',
  'Odyssey',
  'City',
  'Pilot',
  'HRV',
  'Other',
  'CRV',
  'Crosstour'],
 'Toyota': ['Land Cruiser',
  'Yaris',
  'Camry',
  'Corolla',
  'Prado',
  'Furniture',
  'Aurion',
  'Rav4',
  'Hilux',
  'FJ',
  'Avalon',
  'Ciocca',
  'Land Cruiser Pickup',
  'Innova',
  'Land Cruiser 70',
  'Previa',
  'Rush',
  'Echo',
  'Avanza',
  'Hiace',
  'C-HR',
  'Coaster',
  'Prius',
  '4Runner'],
 'Chevrolet': ['Impala',
  'Tahoe',
  'Malibu',
  'Suburban',
  'Caprice',
  'Camaro',
  'Traverse',
  'Spark',
  'Silverado',
  'Cruze',
  'Aveo',
  'Blazer',
  'Lumina',
  'Optra',
  'Kaptiva',
  'Abeka',
  'Colorado',
  'Trailblazer'],
 'Mercedes': ['CLA',
  'E',
  'S',
  'C',
  'GLC',
  'SL',
  'A',
  'ML',
  'CLS',
  'Viano',
  'CL',
  'GL',
  'G',
  'GLE'],
 'MINI': ['Copper', 'Countryman'],
 'Lexus': ['RX', 'ES', 'LX', 'GX', 'NX', 'UX', 'GS', 'LS', 'IS', 'RC'],
 'Land Rover': ['Range Rover', 'Discovery'],
 'GMC': ['Yukon',
  'Sierra',
  'Acadia',
  'Suburban',
  'Safari',
  'Terrain',
  'Envoy'],
 'Mazda': ['CX9', '6', 'CX5', '3', '2', 'CX3', 'CX7'],
 'Ford': ['Expedition',
  'Taurus',
  'Explorer',
  'F150',
  'Flex',
  'Focus',
  'Echo Sport',
  'Vego',
  'Fusion',
  'Victoria',
  'Marquis',
  'Mustang',
  'Edge',
  'Other',
  'Van',
  'Ranger'],
 'Kia': ['Cadenza',
  'Picanto',
  'Optima',
  'Cerato',
  'Cores',
  'Rio',
  'Carnival',
  'Soul',
  'Sportage',
  'Seltos',
  'Carenz',
  'Sorento',
  'K5',
  'Stinger',
  'Mohave',
  'Opirus',
  'Carens',
  'Sedona',
  'Pegas'],
 'Genesis': ['Platinum',
  'G80',
  'Royal',
  'G70',
  'Prestige',
  'Prestige Plus',
  'Coupe',
  'G330'],
 'Cadillac': ['CT-S', 'XT5', 'CT5', 'CT4', 'Escalade', 'ATS', 'CT6', 'Other'],
 'Geely': ['EC7',
  'EC8',
  'Emgrand',
  'Coolray',
  'X7',
  'GS',
  'Other',
  'Azkarra',
  'GC7'],
 'MG': ['ZS', 'RX5', '3', '6', '5', 'RX8', '360', 'GS', 'HS'],
 'Jeep': ['Grand Cherokee',
  'Cherokee',
  'Wrangler',
  'Compass',
  'Patriot',
  'Liberty'],
 'INFINITI': ['M', 'QX', 'Q', 'FX'],
 'Dodge': ['Charger', 'Challenger', 'Durango', 'Ram', 'Nitro'],
 'Ferrari': ['GTB 599 Fiorano'],
 'Great Wall': ['Power', 'Wingle'],
 'Jaguar': ['F-Pace', 'XJ', 'F Type', 'XF'],
 'GAC': ['GS8', 'GS3'],
 'Renault': ['Symbol',
  'Fluence',
  'Duster',
  'Dokker',
  'Talisman',
  'Safrane',
  'Capture',
  'Koleos',
  'Logan',
  'Megane'],
 'Suzuki': ['APV',
  'Vitara',
  'Jimny',
  'Grand Vitara',
  'Ertiga',
  'Dzire',
  'SX4',
  "D'max"],
 'Peugeot': ['3008', '5008', 'Partner', '301', 'Boxer', '307'],
 'Changan': ['Seven', 'Eado', 'CS35', 'CS75', 'CS35 Plus', 'CS85', 'CS95'],
 'HAVAL': ['H6', 'H2', 'H9'],
 'BMW': ['The 7', 'The 4', 'The 5', 'X', 'The 6', 'The 3', 'The M', 'Z'],
 'Porsche': ['911',
  'Panamera',
  'Cayenne',
  'Macan',
  'Cayman',
  'Cayenne S',
  'Cayenne Turbo'],
 'Mitsubishi': ['Attrage',
  'Pajero',
  'Montero',
  'Outlander',
  'Other',
  'L200',
  'ASX',
  'Nativa',
  'Lancer',
  'L300',
  'Galant'],
 'Subaru': ['Forester'],
 'Zhengzhou': ['Pick up'],
 'Lincoln': ['Navigator', 'MKS', 'MKX', 'MKZ', 'Town Car', 'Continental GT'],
 'Daihatsu': ['Gran Max', 'Delta', 'Terios Ground', 'Terios'],
 'FAW': ['T77', 'B50', 'X40'],
 'Chery': ['Tiggo', 'QQ'],
 'Isuzu': ['D-MAX', 'Dyna'],
 'Audi': ['A6', 'Q5', 'S5', 'A8', 'A3', 'S8', 'A5', 'A7', 'Q7', 'A4'],
 'Volkswagen': ['Touareg',
  'Passat',
  'CC',
  'Golf',
  'Beetle',
  'Jetta',
  'Tiguan'],
 'Fiat': ['500', 'Doblo'],
 'Mercury': ['Milan', 'Grand Marquis', 'Montero2'],
 'Hummer': ['H3', 'H-2'],
 'BYD': ['F3'],
 'Maserati': ['Gamble', 'Quattroporte'],
 'Lifan': ['LF X60'],
 'Bentley': ['Flying Spur'],
 'Foton': ['Mini Van', 'Suvana'],
 'Aston Martin': ['DB9'],
 'Other': ['Other'],
 'Victory Auto': ['Van R'],
 'Škoda': ['Fabia', 'Superb'],
 'Iveco': ['Daily']}

origins = ['Saudi', 'Gulf Arabic', 'Other', 'Unknown']

colors = ['Black', 'Silver', 'Grey', 'Navy', 'White', 'Bronze',
       'Another Color', 'Golden', 'Brown', 'Blue', 'Red', 'Oily', 'Green',
       'Orange', 'Yellow']

options = ['Full', 'Standard', 'Semi Full']

fuel_types = ['Gas', 'Diesel', 'Hybrid']

gear_types = ['Automatic', 'Manual']

regions = ['Riyadh', 'Jeddah', 'Dammam', 'Al-Medina', 'Qassim', 'Makkah',
       'Jazan', 'Aseer', 'Al-Ahsa', 'Sabya', 'Khobar', 'Abha', 'Al-Baha',
       'Tabouk', 'Yanbu', 'Hail', 'Al-Namas', 'Jubail', 'Al-Jouf',
       'Hafar Al-Batin', 'Taef', 'Najran', 'Arar', 'Wadi Dawasir',
       'Besha', 'Qurayyat', 'Sakaka']