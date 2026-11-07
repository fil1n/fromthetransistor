module mux2to1(
    input logic r1, 
    input logic r2,
    
    input logic s1,

    output logic y
);
    assign y = (!s1 & r1) | (s1 & r2);
endmodule


module mux4to1(
    input logic r1,
    input logic r2,
    input logic r3,
    input logic r4,

    input logic s1,
    input logic s2,

    output logic y
);
    assign y = (r1 & !s1 & !s2) | (r2 & !s1 & s2) | (r3 & s1 & !s2) | (r4 & s1 & s2);    
endmodule


module mux8to1 (
    input logic r1,
    input logic r2,
    input logic r3,
    input logic r4,
    input logic r5,
    input logic r6,
    input logic r7,
    input logic r8,

    input logic s1,
    input logic s2,
    input logic s3,

    output logic y
);
    wire gate1_out;
    wire gate2_out;

    mux4to1 gate1 (
        .r1(r1),
        .r2(r2),
        .r3(r3),
        .r4(r4),

        .s1(s2),
        .s2(s3),

        .y(gate1_out)
    );

    mux4to1 gate2 (
        .r1(r5),
        .r2(r6),
        .r3(r7),
        .r4(r8),

        .s1(s2),
        .s2(s3),

        .y(gate2_out)
    );

    mux2to1 gate3 (
        .r1(gate1_out),
        .r2(gate2_out),

        .s1(s1),

        .y(y)
    );

endmodule