TRUNCATE TABLE Planeten;

INSERT INTO Planeten ( Planeet 1, Planeet 2 ,Planeet 3, Planeet 4 ,Planeet 5, Planeet 6 , Planeet 7 )
VALUES ( 'Zon', 'Mercurius', 'Venus', 'Aarde', 'Mars' , 'Maan' , 'Mars' );

              ALTER TABLE Planeten 
                 ADD Planeten ( diameter, de afstand tot de zon, de massa ten opzichte van de aarde )
                VALUES  ( '1.392.000' , '4.880' , '12.104' , '12.756' , '6.794' )
              ( ' ' , '57.910.000', '108.208.930' , '149.597.870', '227.936.640')
              ( '332.946', '0,1' , '0,9'  '1' , '0.1' );
              
           
