module mux2(
    input logic r1, 
    input logic r2,
    
    input logic s1,

    output logic y
);
    assign y = (!s1 & r1) | (s1 & r2);
endmodule

